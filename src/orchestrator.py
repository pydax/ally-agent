import os
import sys

# Get the absolute path of the 'ally-agent' root directory
# __file__ is /Users/ujjwalsharma/code/ally-agent/src/orchestrator.py
# parent 1 is /src, parent 2 is /ally-agent
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Inject the root folder at the very front of Python's search array
if root_path not in sys.path:
    sys.path.insert(0, root_path)

from rich.console import Console
from rich.panel import Panel

# Import with the full path from the root directory
from src.agents import EnterpriseLearningAgents

console = Console()

def run_pipeline():
    console.print(Panel.fit("[bold cyan]AllyAgent Execution Console[/bold cyan]\n[Enterprise Learning Framework Core Orchestrator]"))
    
    engine = EnterpriseLearningAgents()
    target_emp = "EMP-001"
    target_role = "Cloud Engineer"
    
    # 1. Curator Run
    curation = engine.learning_path_curator(target_role)
    console.print(f"[bold green]✔[/bold green] [Learning Path Curator] Target Cert mapped to: [yellow]{curation['target_certification']}[/yellow]")
    
    # 2. Plan Generation Run
    plan = engine.study_plan_generator(target_emp, curation)
    console.print(f"[bold green]✔[/bold green] [Study Plan Generator] Output validated. Milestones: [bold]{len(plan.milestones)}/3 Max Limit[/bold].")
    
    # 3. Engagement Context Check
    engagement = engine.engagement_agent(target_emp)
    console.print(f"[bold green]✔[/bold green] {engagement}")
    
    # 4. Evaluator Loop Run
    evaluation = engine.assessment_agent(target_emp)
    console.print(f"[bold green]✔[/bold green] [Assessment Agent] System check: {evaluation['status']} (Current Avg: {evaluation['historical_average']})")
    
    # 5. Management Profile Extraction
    insights = engine.manager_insights_agent()
    console.print("\n[bold magenta]📊 Manager Readiness Insights Summary:[/bold magenta]")
    console.print(f" - System Vector: {insights['risk_summary']}")
    console.print(f" - Metadata Source: {insights['source_doc']}")

if __name__ == "__main__":
    run_pipeline()