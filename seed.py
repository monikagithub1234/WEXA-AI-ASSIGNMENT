from database import driver

def seed_database():
    with driver.session() as session:

        # Clear existing graph
        session.run("MATCH (n) DETACH DELETE n")

        query = """
        // ================= AI Engineer =================
        CREATE (ai:Career {name:'AI Engineer'})
        CREATE (python:Skill {name:'Python'})
        CREATE (sql:Skill {name:'SQL'})
        CREATE (ml:Skill {name:'Machine Learning'})
        CREATE (dl:Skill {name:'Deep Learning'})
        CREATE (course1:Course {name:'Python Bootcamp'})
        CREATE (course2:Course {name:'Machine Learning Course'})
        CREATE (job1:Job {title:'AI Engineer'})
        CREATE (company1:Company {name:'Google'})

        CREATE (ai)-[:REQUIRES]->(python)
        CREATE (ai)-[:REQUIRES]->(sql)
        CREATE (ai)-[:REQUIRES]->(ml)
        CREATE (ml)-[:LEADS_TO]->(dl)

        CREATE (python)-[:HAS_COURSE]->(course1)
        CREATE (ml)-[:HAS_COURSE]->(course2)

        CREATE (ai)-[:QUALIFIES_FOR]->(job1)
        CREATE (company1)-[:POSTS]->(job1)

        // ================= Frontend =================
        CREATE (frontend:Career {name:'Frontend Developer'})
        CREATE (html:Skill {name:'HTML'})
        CREATE (css:Skill {name:'CSS'})
        CREATE (js:Skill {name:'JavaScript'})
        CREATE (react:Skill {name:'React'})
        CREATE (course3:Course {name:'React Bootcamp'})
        CREATE (job2:Job {title:'Frontend Developer'})
        CREATE (company2:Company {name:'Netflix'})

        CREATE (frontend)-[:REQUIRES]->(html)
        CREATE (frontend)-[:REQUIRES]->(css)
        CREATE (frontend)-[:REQUIRES]->(js)
        CREATE (frontend)-[:REQUIRES]->(react)

        CREATE (react)-[:HAS_COURSE]->(course3)
        CREATE (frontend)-[:QUALIFIES_FOR]->(job2)
        CREATE (company2)-[:POSTS]->(job2)

        // ================= Backend =================
        CREATE (backend:Career {name:'Backend Developer'})
        CREATE (flask:Skill {name:'Flask'})
        CREATE (django:Skill {name:'Django'})
        CREATE (api:Skill {name:'REST API'})
        CREATE (course4:Course {name:'Flask Masterclass'})
        CREATE (job3:Job {title:'Backend Developer'})
        CREATE (company3:Company {name:'Microsoft'})

        CREATE (backend)-[:REQUIRES]->(python)
        CREATE (backend)-[:REQUIRES]->(sql)
        CREATE (backend)-[:REQUIRES]->(flask)
        CREATE (backend)-[:REQUIRES]->(django)
        CREATE (backend)-[:REQUIRES]->(api)

        CREATE (flask)-[:HAS_COURSE]->(course4)
        CREATE (backend)-[:QUALIFIES_FOR]->(job3)
        CREATE (company3)-[:POSTS]->(job3)

        // ================= Full Stack =================
        CREATE (fullstack:Career {name:'Full Stack Developer'})
        CREATE (node:Skill {name:'Node.js'})
        CREATE (course5:Course {name:'Full Stack Bootcamp'})
        CREATE (job4:Job {title:'Full Stack Developer'})
        CREATE (company4:Company {name:'Amazon'})

        CREATE (fullstack)-[:REQUIRES]->(html)
        CREATE (fullstack)-[:REQUIRES]->(css)
        CREATE (fullstack)-[:REQUIRES]->(js)
        CREATE (fullstack)-[:REQUIRES]->(node)

        CREATE (node)-[:HAS_COURSE]->(course5)
        CREATE (fullstack)-[:QUALIFIES_FOR]->(job4)
        CREATE (company4)-[:POSTS]->(job4)

        // ================= Data Scientist =================
        CREATE (ds:Career {name:'Data Scientist'})
        CREATE (pandas:Skill {name:'Pandas'})
        CREATE (numpy:Skill {name:'NumPy'})
        CREATE (course6:Course {name:'Data Science Bootcamp'})
        CREATE (job5:Job {title:'Data Scientist'})
        CREATE (company5:Company {name:'IBM'})

        CREATE (ds)-[:REQUIRES]->(python)
        CREATE (ds)-[:REQUIRES]->(pandas)
        CREATE (ds)-[:REQUIRES]->(numpy)
        CREATE (ds)-[:REQUIRES]->(ml)

        CREATE (pandas)-[:HAS_COURSE]->(course6)
        CREATE (ds)-[:QUALIFIES_FOR]->(job5)
        CREATE (company5)-[:POSTS]->(job5)

        // ================= Cloud =================
        CREATE (cloud:Career {name:'Cloud Engineer'})
        CREATE (aws:Skill {name:'AWS'})
        CREATE (docker:Skill {name:'Docker'})
        CREATE (k8s:Skill {name:'Kubernetes'})
        CREATE (course7:Course {name:'AWS Cloud Practitioner'})
        CREATE (job6:Job {title:'Cloud Engineer'})
        CREATE (company6:Company {name:'Oracle'})

        CREATE (cloud)-[:REQUIRES]->(aws)
        CREATE (cloud)-[:REQUIRES]->(docker)
        CREATE (cloud)-[:REQUIRES]->(k8s)

        CREATE (aws)-[:HAS_COURSE]->(course7)
        CREATE (cloud)-[:QUALIFIES_FOR]->(job6)
        CREATE (company6)-[:POSTS]->(job6)

        // ================= Cyber Security =================
        CREATE (cyber:Career {name:'Cyber Security Engineer'})
        CREATE (network:Skill {name:'Networking'})
        CREATE (linux:Skill {name:'Linux'})
        CREATE (ethical:Skill {name:'Ethical Hacking'})
        CREATE (course8:Course {name:'Cyber Security Essentials'})
        CREATE (job7:Job {title:'Cyber Security Engineer'})
        CREATE (company7:Company {name:'Cisco'})

        CREATE (cyber)-[:REQUIRES]->(network)
        CREATE (cyber)-[:REQUIRES]->(linux)
        CREATE (cyber)-[:REQUIRES]->(ethical)

        CREATE (ethical)-[:HAS_COURSE]->(course8)
        CREATE (cyber)-[:QUALIFIES_FOR]->(job7)
        CREATE (company7)-[:POSTS]->(job7)
        """

        session.run(query)
        print("✅ Graph database seeded successfully!")

if __name__ == "__main__":
    seed_database()