from neo4j import GraphDatabase
from config import NEO4J_CONFIG

driver = GraphDatabase.driver(NEO4J_CONFIG['uri'], auth=NEO4J_CONFIG['auth'])
with driver.session() as session:
    cypher="CREATE (a:Symptom{name:'头痛'})-[:dis_to_sym]->(b:Disease{name:'感冒'})"
    record=session.run(cypher)
    result=list(map(lambda x:x[0],record))
    print(result)

