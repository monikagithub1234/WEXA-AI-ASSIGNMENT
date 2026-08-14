from database import driver

def get_career_details(career_name):
    with driver.session() as session:

        query = """
        MATCH (c:Career)
        WHERE toLower(c.name) CONTAINS toLower($career)

        OPTIONAL MATCH (c)-[:REQUIRES]->(s:Skill)
        OPTIONAL MATCH (s)-[:HAS_COURSE]->(course:Course)
        OPTIONAL MATCH (c)-[:QUALIFIES_FOR]->(j:Job)
        OPTIONAL MATCH (company:Company)-[:POSTS]->(j)

        RETURN
        c.name AS career,
        collect(DISTINCT s.name) AS skills,
        collect(DISTINCT course.name) AS courses,
        collect(DISTINCT j.title) AS jobs,
        collect(DISTINCT company.name) AS companies
        LIMIT 1
        """

        result = session.run(query, career=career_name)
        return result.single()