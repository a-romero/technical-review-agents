import warnings
from docproc import chunk_document
from crewai import Crew, Process
from tasks import Tasks
from agents import Agents
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

warnings.filterwarnings('ignore')

llm = ChatGroq(temperature=0.3, model_name="llama3-8b-8192")

manager_llm = ChatAnthropic(model_name="claude-3-5-sonnet-20240620")

chunks = chunk_document("data/GenAI_Chapter10.pdf")

tasks = Tasks()
agents = Agents()

content_reviewer = agents.content_reviewer(llm)
qa_content_reviewer = agents.qa_content_reviewer(llm)

for chunk in chunks:

    review_content = tasks.review_content(content_reviewer, chunk)
    qa_review_content = tasks.qa_review_content(qa_content_reviewer, review_content)

    crew = Crew(
        agents=[
            content_reviewer, 
            qa_content_reviewer
        ],
        tasks=[
            review_content, 
            qa_review_content
        ],
        manager_llm=manager_llm,
        process=Process.hierarchical,
        verbose=False,
        #memory=True
    )

    task_output = crew.kickoff()
    print(task_output)
    with open("revision_chapter10_llama3-8b-8192.txt", "a") as output_file:
        output_file.write(review_content.output.raw_output)