import os

import pandas as pd

from cfg.logging_config import LoggingConfig

logger = LoggingConfig.get_active_logger(__name__)


class PandasUtils:

    @staticmethod
    def get_first_notNA_value(df_slice):
        value = None
        for i in df_slice:
            if not pd.isna(i):
                value = i
                break
        return value

    @staticmethod
    def output_csv_file(
        df, output_path, index=False, mode="w", encoding="utf-8-sig", header=True
    ):
        filename = os.path.basename(output_path)

        logger.info(f"Solicitada a impressao do arquivo {filename}")
        logger.info(f"Path: {output_path}")

        df.to_csv(
            output_path,
            sep=";",
            decimal=",",
            mode=mode,
            index=index,
            encoding=encoding,
            header=header,
        )

        logger.info("Arquivo Impresso")
