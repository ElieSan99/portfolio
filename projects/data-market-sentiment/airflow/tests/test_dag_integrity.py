import unittest
from airflow.models import DagBag


class TestDagIntegrity(unittest.TestCase):
    def setUp(self):
        self.dagbag = DagBag(dag_folder="airflow/dags", include_examples=False)

    def test_dag_loads_with_no_errors(self):
        self.assertEqual(
            len(self.dagbag.import_errors),
            0,
            f"Erreurs d'importations : {self.dagbag.import_errors}",
        )

    def test_reddit_dag_present(self):
        dag = self.dagbag.get_dag(dag_id="reddit_ingestion_pipeline")
        self.assertIsNotNone(dag)
        self.assertEqual(len(dag.tasks), 1)
