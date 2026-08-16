### WEXA AI — CognoDB Graph Database Take-Home Assignment

**Career Graph Advisor** is a graph-powered web application that helps users explore career paths by discovering relationships between **careers, skills, courses, job roles, and companies**.

The application is backed by **CognoDB**, a managed graph database, and uses the official **Neo4j Python Driver** to execute parameterized openCypher queries over the Bolt protocol.

---

## 🎯 Project Objective

Choosing a career is not only about identifying a job title. A career is connected to many other concepts such as skills, courses, job roles, and companies.

Career Graph Advisor models these relationships as a graph and provides a simple interface for users to explore career information.

Example:

```text
Career
  │
  ├── REQUIRES ──────> Skill
  │
  ├── RECOMMENDS ────> Course
  │
  ├── LEADS_TO ──────> Job Role
  │
  └── AVAILABLE_AT ─> Company
```

This project was developed as part of the **WEXA AI Candidate Take-Home Assignment — Build a Graph Database Application**.

---

# ✨ Features

* 🔍 Search for careers
* 🛠️ Discover required skills
* 📚 Find relevant courses
* 💼 Explore related job roles
* 🏢 Discover associated companies
* 🕸️ Graph-based relationship modeling
* 🔗 Multi-hop graph traversal
* ⚡ Parameterized Cypher queries
* 🌐 Flask-based web application
* 🎨 Clean and responsive UI
* ⏳ Loading and result states
* 📭 Empty-result handling
* ⚠️ Graceful database error handling
* 🔐 Environment-based database credentials

---

# 🧠 Why a Graph Database?

The interesting part of a career recommendation system is the **relationships between entities**, rather than simply storing independent records.

In a relational database, finding relationships such as:

```text
Backend Developer
        ↓
      Python
        ↓
Python Course
        ↓
Another Career
```

may require multiple tables and JOIN operations.

With a graph database, these relationships are represented directly as nodes and edges.

For example:

```text
(Career)-[:REQUIRES]->(Skill)

(Career)-[:RECOMMENDS]->(Course)

(Career)-[:LEADS_TO]->(JobRole)

(Career)-[:AVAILABLE_AT]->(Company)
```

This makes connected-data queries and multi-hop traversal natural and easy to express.

### Example Graph Exploration

A user searching for:

```text
Backend Developer
```

can discover:

```text
Backend Developer
       │
       ├── Python
       ├── SQL
       ├── Flask
       ├── Django
       └── REST API
              │
              └── Related careers
```

This relationship-driven exploration is where a graph database provides a strong advantage over a traditional relational schema.

---

# 🗺️ Graph Data Model

## Graph Diagram

```text
                    ┌──────────────┐
                    │    Career    │
                    └──────┬───────┘
                           │
             ┌─────────────┼──────────────┐
             │             │              │
          REQUIRES      RECOMMENDS     LEADS_TO
             │             │              │
             ▼             ▼              ▼
        ┌─────────┐   ┌─────────┐   ┌──────────┐
        │  Skill  │   │ Course  │   │ JobRole  │
        └────┬────┘   └─────────┘   └────┬─────┘
             │                           │
             │ RELATED_TO                │
             ▼                           ▼
        ┌─────────┐                 ┌─────────┐
        │  Skill  │                 │ Company │
        └─────────┘                 └─────────┘
```

## Node Types

| Node      | Description                                  |
| --------- | -------------------------------------------- |
| `Career`  | A career path such as Backend Developer      |
| `Skill`   | Technical skill required for a career        |
| `Course`  | Learning resource associated with a career   |
| `JobRole` | Professional role related to a career        |
| `Company` | Company associated with career opportunities |

## Relationships

| Relationship   | Description                                           |
| -------------- | ----------------------------------------------------- |
| `REQUIRES`     | A career requires a skill                             |
| `RECOMMENDS`   | A career recommends a course                          |
| `LEADS_TO`     | A career is associated with a job role                |
| `AVAILABLE_AT` | A career/job opportunity is associated with a company |
| `RELATED_TO`   | Connects related skills or concepts                   |

---

# 🛠️ Technology Stack

### Backend

* Python
* Flask
* Neo4j Python Driver

### Database

* CognoDB
* openCypher
* Bolt Protocol

### Frontend

* HTML5
* CSS3
* JavaScript

### Tools

* Git
* GitHub
* Python Virtual Environment

---

# 📂 Project Structure

```text
Career-Graph-Advisor/
│
├── app.py
├── seed.py
│
├── queries/
│   └── queries.cypher
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── screenshots/
│   ├── home.png
│   └── results.png
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ☁️ CognoDB Setup

## 1. Create a CognoDB Account

Create an account at:

**https://console.cognodb.com/signup**

The free tier does not require a credit card.

## 2. Create a Free Instance

Create a free **c0** instance from the CognoDB Cloud console and select a region.

The instance provides a connection URI similar to:

```text
bolt+s://<instance-id>.databases.cognodb.cloud
```

## 3. Save the Database Credentials

CognoDB generates a password for the `cognodb` user.

The password is displayed once, so save it securely.

Do **not** commit it to GitHub.

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
COGNODB_URI=bolt+s://<your-instance-id>.databases.cognodb.cloud
COGNODB_USERNAME=cognodb
COGNODB_PASSWORD=your_password
```

The `.env` file is excluded from Git using `.gitignore`.

Example `.env.example`:

```env
COGNODB_URI=
COGNODB_USERNAME=cognodb
COGNODB_PASSWORD=
```

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/career-graph-advisor.git
cd career-graph-advisor
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create the `.env` file and add the CognoDB connection details.

---

# 🌱 Seed the Database

The project includes a seed script containing realistic career-related data.

Run:

```bash
python seed.py
```

The script creates nodes and relationships such as:

```text
Backend Developer
       │
       ├── Python
       ├── SQL
       ├── Flask
       ├── Django
       ├── REST API
       │
       ├── Python Bootcamp
       ├── Flask Masterclass
       │
       └── Microsoft
```

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

# 🔎 Main Cypher Queries

The application communicates with CognoDB using the official Neo4j Python driver.

All user-provided values are passed as **query parameters** rather than being concatenated into Cypher strings.

## 1. Career Information Query

```cypher
MATCH (c:Career {name: $career})
OPTIONAL MATCH (c)-[:REQUIRES]->(s:Skill)
OPTIONAL MATCH (c)-[:RECOMMENDS]->(course:Course)
OPTIONAL MATCH (c)-[:LEADS_TO]->(role:JobRole)
OPTIONAL MATCH (c)-[:AVAILABLE_AT]->(company:Company)
RETURN c,
       collect(DISTINCT s) AS skills,
       collect(DISTINCT course) AS courses,
       collect(DISTINCT role) AS roles,
       collect(DISTINCT company) AS companies
```

The career name is passed as a parameter:

```python
session.run(query, career=career_name)
```

This avoids unsafe string-concatenated Cypher.

---

# 🔗 Multi-Hop Graph Traversal

The application also demonstrates multi-hop traversal.

For example, related careers can be discovered through shared skills:

```cypher
MATCH (c:Career)-[:REQUIRES]->(s:Skill)<-[:REQUIRES]-(other:Career)
WHERE c.name = $career
RETURN DISTINCT other
```

The traversal is:

```text
Career
   ↓
 Skill
   ↑
Career
```

This demonstrates how graph traversal can discover connections between careers based on their shared skills.

---

# 🧩 Why This Query Is Graph-Friendly

Consider:

```text
Backend Developer
        │
        └── Python
              │
              └── Data Engineer
```

The graph can directly traverse relationships to discover related careers.

In a relational database, this type of relationship-based discovery could require several tables and JOIN operations.

The graph representation makes connected-data exploration more direct and expressive.

---

# 🖥️ User Interface

Career Graph Advisor provides a simple interface designed for non-technical users.

The user enters a career such as:

```text
Backend Developer
```

and receives connected information including:

### 🛠️ Skills

* Python
* SQL
* Flask
* Django
* REST API

### 📚 Courses

* Python Bootcamp
* Flask Masterclass

### 💼 Job Roles

* Backend Developer

### 🏢 Companies

* Microsoft

---

# 📸 Screenshots

## Career Search Interface

<img width="1920" height="915" alt="{736DC04D-E41D-4944-954C-36F1A0F07843}" src="https://github.com/user-attachments/assets/5979160b-c3b3-4c6b-95c2-cd6ba2587fd4" />


## Career Results

<img width="1920" height="913" alt="{BFB49121-D9D9-4CE7-BFED-384A47A1A319}" src="https://github.com/user-attachments/assets/0a78136e-16d7-48f8-8150-d186dcc3a6bf" />

<img width="1920" height="909" alt="{C01A23F4-14EB-4953-936E-B63BE631A302}" src="https://github.com/user-attachments/assets/bf230af4-7f48-4f07-a109-7e05a49fac80" />


# ⚠️ Error Handling

The application handles database connectivity problems gracefully.

If CognoDB is unavailable, the application displays a user-friendly message instead of exposing raw database errors.

Example:

```text
Unable to connect to the career database.

Please try again later.
```

Database credentials are never exposed to the frontend.

---

# 🔒 Security

The application follows basic security practices:

* Database credentials are stored in environment variables.
* `.env` is excluded from Git.
* Cypher queries use parameters.
* Credentials are never hard-coded.
* Database errors are handled without exposing sensitive information.

---

# 🧪 Example User Flow

```text
User opens Career Graph Advisor
            ↓
Enters a career
            ↓
Clicks Search
            ↓
Flask receives the request
            ↓
Parameterized Cypher query
            ↓
CognoDB graph database
            ↓
Graph relationships are traversed
            ↓
Flask processes the results
            ↓
Career information displayed
```

---

# 🚀 Future Enhancements

Possible future improvements include:

* 🤖 AI-powered personalized career recommendations
* 📊 Skill-gap analysis
* 🗺️ Personalized learning roadmaps
* 🔗 Interactive graph visualization
* 💼 Job vacancy integration
* 💰 Salary information
* 📈 Career progression paths
* 👤 User profiles
* 📚 Additional learning resources
* 🎯 Career similarity recommendations

---

# 🌐 Demo

### Hosted Application

https://wexa-ai-assignment-beryl.vercel.app/

### Screen Recording

https://drive.google.com/file/d/1deFbvyLEOuKWzxfP25BwZheeXxPxLvwu/view?usp=drivesdk
---

# 📧 Submission

https://github.com/monikagithub1234/WEXA-AI-ASSIGNMENT

# 🎯 What This Project Demonstrates

Career Graph Advisor demonstrates practical experience with:

* Graph data modeling
* CognoDB integration
* openCypher query design
* Multi-hop graph traversal
* Parameterized database queries
* Python backend development
* Flask web application development
* Database integration
* Environment-based configuration
* Error handling
* Frontend UI development
* Git/GitHub project organization

The goal of the project is not simply to store career information, but to model the **relationships between career concepts** and make those relationships useful through an interactive web application.

---

# 👩‍💻 Author

**Monika Priya**

B.Tech — Computer Science & Engineering
Specialization — Artificial Intelligence & Machine Learning

---

## ⭐ Career Graph Advisor

**A graph-powered career exploration application built with Flask and CognoDB.**

Developed for the **WEXA AI CognoDB Take-Home Assignment**.
