import lmql

@lmql.query
async def hello():
    '''
    argmax "Hello[WHO]" from "openai/gpt-4" where len(WHO) < 10
    '''
    
    await hello()[0].prompt