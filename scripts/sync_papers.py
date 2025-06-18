import json

def get_markdown_table(data_path="data/papers.json"):
    with open(data_path) as f: papers = json.load(f)
    lines = ["| Benchmark | Year | Category | arXiv |", "| :--- | :--- | :--- | :--- |"]
    for p in papers:
        lines.append(f"| **{p['name']}** | {p['year']} | `{p['category']}` | [{p['arxiv_id']}](https://arxiv.org/abs/{p['arxiv_id']}) |")
    return "\n".join(lines)

if __name__ == "__main__":
    print(get_markdown_table())
