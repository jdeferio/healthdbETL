import itertools
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# set logging
logging.basicConfig(level=logging.info)
logger = logging.getLogger()


class ETL(object):
    def __init__(
        self, session=None, engine=None, df=None, col_map=None, commit_session=True
    ):
        self.session = session
        self.engine = engine
        self.df = df
        self.col_map = col_map
        self.commit_session = commit_session
        self.failed_chunks = []
        self.count = 0

    def prepare_table(self, df):
        cols = [c[0] for c in self.col_map]
        missing_cols = set(cols) - set(df.columns)
        if missing_cols:
            logger.info(f"missing columns identified: {missing_cols}")
        df = df.loc[:, cols].rename(columns={k: v for k, v in self.col_map})
        return df

    def load_chunk(self, chunk):
        try:
            self.session.add_all(chunk)
            if self.commit_session:
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            self.failed_chunks.append((e, chunk))
            logger.info(f"failed to load chunk: {e}")
            logger.info(f"rollback performed")

    def load_data(self, objects, chunksize=50):
        self.failed_chunks = []
        bins = range(0, len(objects), chunksize)
        for b in bins:
            self.load_chunk(objects[b : b + chunksize])
        objects = list(itertools.chain(*[e[1] for e in self.failed_chunks]))
        if (self.count == 0) and (len(objects) > 0):
            self.count += 1
            self.load_data(objects, chunksize=1)
