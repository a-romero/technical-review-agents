from crewai import Agent

class Agents():

    def content_reviewer(self, llm):
        return Agent(
            llm=llm,
            role="Senior Technical Content Reviewer",
            goal="Verify technical content for consistency, accuracy and completeness. Produce comments against each chunk of text that you receive: {chunk}.",
            backstory="You are a veteran Technical Content Reviewer in the Information Technology arena ensuring that the content of each {chunk} that is passed on to you is accurate and consistent from a technical perspective."
                        "You produce very well structured comments that address the following areas:"
                        "- What is not correct, accurate, consistent or complete in the {chunk}"
                        "- Why is the information in the {chunk} not correct, accurate, consistent or complete"
                        "- How can the information in the {chunk} be corrected, made accurate, consistent or complete",
            allow_delegation=False,
        )
    
    #def code_tester(self,llm):
    #    return Agent(
    #        llm=llm,
    #        role="Senior Technical Content Reviewer",
    #        goal="Find the most performing strategies of investing money.",
    #        backstory="You are a veteran investor looking to advise customers on what to invest their money in.",
    #        allow_delegation=False,
    #    )
    
    def qa_content_reviewer(self, llm):
        return Agent(
            llm=llm,
            role="Quality Assurance Specialist",
            goal="Get recognition for providing the best quality assurance in your team",
            backstory="You are working with the rest of the team on a project that requires a high level of quality assurance. You are responsible for ensuring that the quality of the work produced by the team is of the highest standard."
                      "You are known for your attention to detail and your ability to identify and rectify any issues that may arise during the project."
                      "Your assignment is to review the work that the Senior Technical Content Reviewer has produced, ensuring that the comments they produce are well structured and address the following areas:"
                        "- There is a clear description in the review comments of what is not correct, accurate, consistent or complete."
                        "- The reasons why the information alluded to in the review comments is not correct, accurate, consistent or complete are clearly stated."
                        "- The review comment provides a clear explanation of how the information alluded to in the review comments can be corrected, made accurate, consistent or complete.",
            allow_delegation=True,
        )