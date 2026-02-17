import unittest
from airflow.models import DagBag


class TestDagIntegrity(unittest.TestCase):
    def setUp(self):
        import os

        # Chemin absolu vers le dossier dags pour éviter les soucis de CWD en CI
        dag_path = os.path.join(os.path.dirname(__file__), "..", "dags")
        self.dagbag = DagBag(dag_folder=dag_path, include_examples=False)

    def test_dag_loads_with_no_errors(self):
        self.assertEqual(
            len(self.dagbag.import_errors),
            0,
            f"Erreurs d'importations : {self.dagbag.import_errors}",
        )

    def test_reddit_dag_present(self):
        # Utiliser l'accès direct au dictionnaire pour éviter les requêtes DB
        dag = self.dagbag.dags.get("reddit_ingestion_pipeline")
        self.assertIsNotNone(
            dag, "Le DAG 'reddit_ingestion_pipeline' n'a pas été trouvé."
        )
        self.assertTrue(len(dag.tasks) >= 1)
