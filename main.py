import os
# 1. 更新导入路径：从 langchain_community 导入工具加载器
from langchain_community.agent_toolkits.load_tools import load_tools
# 2. 更新导入路径：使用官方推荐的 langchain_openai
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

# 设置环境变量
os.environ["OPENAI_API_KEY"] = 'sk_OPtzaEF3NJHjY8wP7eO5-_7ukvqLgZ0U47ZArfma3d4' # 建议尽快重置此Key，因为已公开
os.environ["SERPAPI_API_KEY"] = '660a315ec151c510645dbfd0de9b57229c4f08d30e23f314f5fc5d8530a32ac9'

# 3. 使用 ChatOpenAI 类
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://api.jiekou.ai/openai", # 保持你的中转地址
    temperature=0
)

# 加载 serpapi 工具
tools = load_tools(["serpapi"])

# 初始化 Agent
# 注意：虽然 initialize_agent 也有警告建议用 LangGraph，但为了保持教程连贯性，
# 这里暂时保留 initialize_agent，改用适合聊天模型的 AgentType
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, # 针对 Chat 模型优化
    verbose=True,  #  开启之后完整的 chain 执行过程。
    handle_parsing_errors=True # 加上这个以防止大模型输出格式微小错误导致程序崩溃
)

# 4. 运行 agent
# .run() 已弃用，改用 .invoke()
try:
    result = agent.invoke({"input": "What's the date today? What great events have taken place today in history?"})
    print(result['output'])
except Exception as e:
    print(f"发生错误: {e}")