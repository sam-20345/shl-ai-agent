class ComparisonEngine:

    def compare(self, assessment1, assessment2):

        return {
            "Assessment 1": {
                "Name": assessment1.get("name", ""),
                "Duration": assessment1.get("duration", ""),
                "Job Levels": assessment1.get("job_levels", []),
                "Languages": assessment1.get("languages", []),
                "Assessment Type": assessment1.get("keys", []),
                "Description": assessment1.get("description", ""),
            },
            "Assessment 2": {
                "Name": assessment2.get("name", ""),
                "Duration": assessment2.get("duration", ""),
                "Job Levels": assessment2.get("job_levels", []),
                "Languages": assessment2.get("languages", []),
                "Assessment Type": assessment2.get("keys", []),
                "Description": assessment2.get("description", ""),
            },
        }