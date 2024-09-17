from review_comment import ReviewComment
from textwrap import dedent
from crewai import Task

class Tasks():
    def review_content(self, agent, chunk):
        return Task(
            description=dedent(f"""\
                               Perform a thorough technical review of the {chunk}. Focus on the following areas:
                               - Consistency
                               - Accuracy
                               - Completeness
                               - Technical correctness
                               Each {chunk} might have several pieces of text and/or code that need reviewing. Produce review-comments against each of them, 
                               ensuring that they are are well structured and address the following questions:
                               - Quote the piece of text that you are reviewing.
                               - What is not correct, accurate, consistent or complete in the {chunk}.
                               - Why is the information in the {chunk} not correct, accurate, consistent or complete.
                               - How can the information in the {chunk} be corrected, made accurate, consistent or complete.
                               """),
            expected_output="""A detailed review-comment of each of the pieces of text and/or code you are reviewing. The comments should be formatted as 
                            shown below:
                            Quote 1: <quoted piece of text>
                            Review-Comment 1: <review-comment using free text>
                            """,
            agent=agent,
        )
    
    def qa_review_content(self, agent, review_content):
        return Task(
            description=dedent(f"""\
                               Perform quality assurance on the review-comments drafted ensuring that:
                                "- There is a clear description in the review-comment of what is not correct, accurate, consistent or complete."
                                "- The reasons why the information alluded to in the quote is not correct, accurate, consistent or complete are clearly 
                                stated."
                                "- The review-comment provides a clear explanation of how the information alluded to can be corrected, made accurate, 
                                consistent or complete."
                                "- Every review-comment addresses a specific issue, and hence discard any review-comments that do not address any issues 
                                or that simply state the text fragment is correct.
                                "- If the review-comment meets your expectations then copy it as is into your revised review-comment output without changing 
                                anything from it.
                                 - If according to your quality assurance standards, the a review-comment needs to be amended to be improved do so in your  
                                output to provide with the revised review-comment."
                               """),
            expected_output="""A final, set of revised review-comments that have been outlined in a professional and friendly tone using the format:
                            Quote 1: <quoted piece of text>
                            Revised Review-Comment 1: <review comment using free text>
                            """,
            context=[review_content],
            agent=agent,
        )