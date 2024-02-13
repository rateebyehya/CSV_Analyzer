##from langchain.agents import create_pandas_dataframe_agent #This import has been recently replaced by the below
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
#from langchain.llms import OpenAI
#New import from langchain, which replaces the above
from langchain_openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI



def query_agent(data, query):

    # Parse the CSV file and create a Pandas DataFrame from its contents.
    df = pd.read_csv(data)

    llm = ChatOpenAI(temperature = 0, model = "gpt-3.5-turbo-0613")
    
    # Create a Pandas DataFrame agent.
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)

    #Python REPL: A Python shell used to evaluating and executing Python commands. 
    #It takes python code as input and outputs the result. The input python code can be generated from another tool in the LangChain

    prompt = {
    "tool_names": ["pandas"],
    "tools": {
        "pandas": {
            "df": df.to_dict()
        }
    },
    "input": str(query)
    }

    return agent.run(prompt)