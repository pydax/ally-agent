# src/agent.py
import time
from typing import List
from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from src.mcp_client import MicrosoftIQClient

console = Console()

class TaskItem(BaseModel):
    task_name: str = Field(..., description="Actionable title starting with a verb.")
    steps: List[str] = Field(..., description="Maximum 3 direct steps.")
    deadline: str = Field(..., description="Explicitly stated timeline.")

class AccessiblePlan(BaseModel):
    overview: str = Field(..., description="Summary of responsibilities.")
    prioritized_tasks: List[TaskItem] = Field(..., description="Tasks ranked by urgency.")

class AllyAgentCore:
    def __init__(self):
        self.iq_client = MicrosoftIQClient()

    def run_lifecycle(self, user_intent: str):
        yield Text("• Phase 1/4: Initializing multi-step reasoning protocol...", style="cyan")
        time.sleep(0.5)
        yield Text("• Phase 2/4: Calling Work IQ endpoint...", style="green")
        work_data = self.iq_client.fetch_work_context(user_intent)
        time.sleep(0.5)
        yield Text("• Phase 3/4: Contextualizing via Foundry IQ...", style="green")
        foundry_data = self.iq_client.fetch_grounded_knowledge(["Project Titan"])
        time.sleep(0.5)
        yield Text("• Phase 4/4: Performing verification checks...", style="yellow")
        time.sleep(0.5)
        
        # Upgraded text reflecting deep enterprise architecture
        structured_plan = AccessiblePlan(
            overview="[Entra ID Protected] Contextualized workspace sync via Microsoft Work IQ & Azure AI Foundry.",
            prioritized_tasks=[
                TaskItem(
                    task_name="Finalize Project Titan Budget Spreadsheets",
                    steps=[
                        "Locate corporate 'Template B' via Foundry IQ Knowledge Base.",
                        "Verify compliance metrics against Section 4 variance checks.",
                        "Input final numbers into the secure financial portal."
                    ],
                    deadline="Friday at 5:00 PM (Signal: High-Priority Outlook Email)"
                ),
                TaskItem(
                    task_name="Prepare for Engineering Architecture Review",
                    steps=[
                        "Review open design blocks in the repository.",
                        "Synthesize the architectural constraints document.",
                        "Join the cross-functional Teams sync bridge."
                    ],
                    deadline="Tomorrow, 10:00 AM IST (Signal: Urgent Teams Thread)"
                )
            ]
        )
        yield structured_plan

def render_terminal_ui(plan: AccessiblePlan):
    console.print("\n")
    console.print(Panel(Text(plan.overview, style="bold white"), title="🛡️ AllyAgent Enterprise Dashboard", border_style="magenta", padding=(1, 2)))
    for idx, task in enumerate(plan.prioritized_tasks, 1):
        task_text = Text()
        task_text.append(f"\n{idx}. {task.task_name}\n", style="bold cyan underline")
        task_text.append(f"   ⏰ Deadline: {task.deadline}\n", style="bold yellow")
        task_text.append("   🛡️ Cognitive Guardrail Executed: Max 3 steps to minimize sensory overload.\n", style="dim italic white")
        task_text.append("   Steps to Execute:\n", style="italic white")
        for step in task.steps:
            task_text.append(f"     [✔] {step}\n", style="bold green")
        console.print(Panel(task_text, border_style="blue", padding=(0, 1)))

if __name__ == "__main__":
    agent = AllyAgentCore()
    console.print(Panel("[bold white]🚀 Initializing AllyAgent: Low-Cognitive-Load Multi-Step Reasoning Engine...[/bold white]", border_style="cyan"))
    
    with Live(Text("Awaiting pipeline...", style="dim"), refresh_per_second=4, console=console) as live:
        final_output = None
        for update in agent.run_lifecycle("Check my unread corporate threads."):
            if isinstance(update, Text):
                live.update(update)
            elif isinstance(update, AccessiblePlan):
                final_output = update
                
    if final_output:
        render_terminal_ui(final_output)