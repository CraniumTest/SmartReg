from nlp_model import NLPModel

def analyze_documents(documents):
    nlp_model = NLPModel()
    results = []
    for document in documents:
        result = nlp_model.extract_compliance_requirements(document)
        results.append(result)
    return results

if __name__ == "__main__":
    documents = [
        "Document content 1",
        "Document content 2",
        # More document content...
    ]
    compliance_results = analyze_documents(documents)
    print(compliance_results)
