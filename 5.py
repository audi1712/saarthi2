def get_utterance(entities: list,utterence: str)->list:
    if utterence.find("<>") == -1:
        return [utterence]
    else:
        res = []
        for i in entities:
            x = utterence.find("<>")
            res+=get_utterance([j for j in entities if j!=i],utterence[:x] + i + utterence[x+2:])
        return res
utterances = ["How far is <> from <>", "How is the weather in <>"]
entities = ["kolkata", "delhi"]
ans = []
for i in utterances:
    ans += get_utterance(entities,i) 
print(ans)