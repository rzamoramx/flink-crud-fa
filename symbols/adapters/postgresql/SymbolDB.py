
import uuid
from symbols.domain.ports.SymbolDBInterface import SymbolDBInterface
import sqlalchemy as db
from symbols.config.conf import postgres_settings as ps
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from typing import get_type_hints
from symbols.domain.model.Symbol import DomainSymbolModel

base = declarative_base()


class Symbol(base):
    __tablename__ = 'Symbol'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Uid = db.Column(db.String, primary_key=True)


# Postgresql logic
class SymbolPostgres(SymbolDBInterface):
    __engine = None

    def __init__(self):
        self.__engine = db.create_engine(
            f"postgresql://{ps.POSTGRES_USER}:{ps.POSTGRES_PASSWORD}@{ps.POSTGRES_HOSTNAME}:{ps.DATABASE_PORT}/{ps.POSTGRES_DB}"
        )
        # for reference: session = sessionmaker(autoflush=False, autocommit=False, bind=self.__engine)()
        self.__init_db()

    def fetch(self, limit: int) -> [dict]:
        symbols = []

        with Session(self.__engine) as session:
            results = session.query(Symbol).limit(limit).all()

        for symbol in results:
            del symbol.__dict__['_sa_instance_state']
            symbols.append(symbol.__dict__)

        return symbols

    def get(self, uid: str) -> dict:
        with Session(self.__engine) as session:
            symbol = session.query(Symbol).filter(Symbol.Uid == uid).first()

        if symbol is not None:
            del symbol.__dict__['_sa_instance_state']
            return symbol.__dict__

        return {}

    def insert(self, symbol: DomainSymbolModel, uid: str) -> dict:
        if uid == "" or uid is None:
            uid = str(uuid.uuid4())

        symb = Symbol()
        symb.Uid = uid
        for key, value in symbol.items():
            setattr(symb, key, value)

        # Here we are using transactions and context manager to close session after transaction
        with Session(self.__engine) as session:
            session.add(symb)
            session.flush()
            session.refresh(symb)
            session.commit()
            # if you get id from symb.Id after the context manager, you will get an error of type detached session,
            # because the context manager call close() method of session, so we use a variable to store it and use later
            result_id = symb.Id

        print(f'inserted with id: {result_id} and uid: {symb.Uid}')
        return symbol.items()

    def update(self, symbol: dict, uid: str):
        # Not used
        pass

    def get_by_symbol(self, symbol: str) -> dict:
        with Session(self.__engine) as session:
            symbol = session.query(Symbol).filter(Symbol.symbol == symbol).first()

        if symbol is not None:
            del symbol.__dict__['_sa_instance_state']
            return symbol.__dict__

        return {}

    def delete_symbol(self, symbol: str) -> bool:
        with Session(self.__engine) as session:
            affected = session.query(Symbol).filter(Symbol.symbol == symbol).delete()
            session.commit()

        return affected > 0

    def __init_db(self):
        inspector = db.inspect(self.__engine)

        if not inspector.has_table("Symbol", schema=ps.POSTGRES_DB):
            for key, val in get_type_hints(DomainSymbolModel).items():
                if val.__name__ == 'float':
                    setattr(Symbol, key, db.Column(db.Float))

                if val.__name__ == 'int':
                    setattr(Symbol, key, db.Column(db.Integer))

                if val.__name__ == 'str':
                    setattr(Symbol, key, db.Column(db.String))

            base.metadata.create_all(self.__engine)
