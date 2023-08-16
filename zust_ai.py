import openai
import gradio  
openai.api_key = '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'

messages = [{"role": "system", "content": """You are a Lawyer who knows the IPC section very well
you will provide applicable IPC sections for there crimes clients on prompting  there crimes also with reference to IPC 
to provide legal advice, argue cases in court, and make judgments"""}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="IPC AI bot")

demo.launch(share=True)
