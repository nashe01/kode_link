# Domain filter stub

def is_in_domain(query):
    # Example: Only allow queries containing certain keywords
    company_keywords = ['product', 'service', 'policy', 'employee', 'support', 'company']
    return any(keyword in query.lower() for keyword in company_keywords) 