import great_expectations as ge
import pandas as pd


class DataValidator:
    def __init__(self):
        pass

    def validate_reddit_posts(self, df):
        """
        Applique des règles de qualité sur les posts Reddit.
        """
        ge_df = ge.from_pandas(df)

        # 1. Vérifier que les colonnes essentielles ne sont pas nulles
        ge_df.expect_column_values_to_not_be_null("post_id")
        ge_df.expect_column_values_to_not_be_null("title")
        ge_df.expect_column_values_to_not_be_null("collected_at")

        # 2. Vérifier l'unicité des IDs
        ge_df.expect_column_values_to_be_unique("post_id")

        # 3. Vérifier que le score est positif ou nul (généralement vrai pour top)
        ge_df.expect_column_values_to_be_between("score", min_value=0)

        # 4. Vérifier les types
        ge_df.expect_column_values_to_be_of_type("author", "str")

        results = ge_df.validate()

        if not results["success"]:
            print("Échec de la validation de qualité !")
            # On pourrait lever une exception ici ou logger les erreurs

        return results["success"]
