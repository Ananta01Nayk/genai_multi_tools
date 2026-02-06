from graph.builder import build_graph


chatbot = build_graph()

def retrieve_all_threads():
    threads = set()
    for cp in chatbot.checkpointer.list(None):
        threads.add(cp.config["configurable"]["thread_id"])
    return list(threads)
