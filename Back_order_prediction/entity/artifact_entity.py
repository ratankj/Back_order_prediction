from collections import namedtuple

#data Ingestion

DataIngestionArtifact = namedtuple('DataIngestionArtifact',
                                   ['train_file_path', 'test_file_path','is_ingested','message'])

DataValidationArtifact = namedtuple('DataValidationArtifact',
                                    ["schema_file_path","is_validated","message"])

