import os
import sys
from pathlib import Path

# Fix module resolution boundaries absolutely
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from src.agents import EnterpriseLearningAgents

console = Console()

def run_pipeline():
    console.print(Panel.fit("[bold green]AllyAgent Engine v2.0: Advanced Multi-Agent Reasoning Loop[/bold green]"))
    
    engine = EnterpriseLearningAgents()
    target_emp = "EMP-001"
    target_role = "Cloud Engineer"
    
    # 1. Curator Action
    curation = engine.learning_path_curator(target_role)
    t1 = Tree(f"[bold cyan]🤖 1. Learning Path Curator[/bold cyan] -> Target: {curation['target_certification']}")
    for thought in curation["agent_thoughts"]:
        t1.add(f"[dim]{thought}[/dim]")
    console.print(t1)
    console.print("---")

    # 2. Study Plan Generation (Planner-Executor + Critic)
    plan = engine.study_plan_generator(target_emp, curation)
    t2 = Tree(f"[bold cyan]🤖 2. Study Plan Generator (Planner-Executor Pattern)[/bold cyan]")
    for thought in plan.reasoning_log:
        if "CRITIC" in thought:
            t2.add(f"[bold yellow]🛡️ {thought}[/bold yellow]")
        else:
            t2.add(f"[dim]{thought}[/dim]")
    console.print(t2)
    console.print(f"   👉 [green]Enforced Guardrail Status:[/green] Passed ({len(plan.milestones)}/3 Milestones allowed)")
    console.print("---")

    # 3. Engagement Monitoring
    engagement = engine.engagement_agent(target_emp)
    t3 = Tree("[bold cyan]🤖 3. Contextual Engagement Agent (Work IQ)[/bold cyan]")
    for thought in engagement["agent_thoughts"]:
        t3.add(f"[dim]{thought}[/dim]")
    console.print(t3)
    console.print("---")

    # 4. Assessment Control
    eval_loop = engine.assessment_agent(target_emp)
    t4 = Tree(f"[bold cyan]🤖 4. Assessment & Evaluation Agent[/bold cyan] -> Decision: [bold red]{eval_loop['status']}[/bold red]")
    for thought in eval_loop["agent_thoughts"]:
        t4.add(f"[dim]{thought}[/dim]")
    console.print(t4)
    console.print("---")

    # 5. Manager Reporting Layer
    insights = engine.manager_insights_agent()
    t5 = Tree("[bold cyan]🤖 5. Privacy-Preserving Manager Insights Agent[/bold cyan]")
    for thought in insights["agent_thoughts"]:
        t5.add(f"[dim]{thought}[/dim]")
    console.print(t5)
    
    console.print("\n[bold magenta]📊 Executive Readiness Dashboard View:[/bold magenta]")
    console.print(f" [bold red]⚠ Risk Indicator:[/bold red] {insights['risk_summary']}")

if __name__ == "__main__":
    run_pipeline()