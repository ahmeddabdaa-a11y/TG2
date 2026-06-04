import asyncio
import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from core.account_manager import AccountManager
from storage.encryption import EncryptionManager
from config.settings import config
import os

app = typer.Typer()
console = Console()

# تهيئة الأنظمة
crypto_manager = EncryptionManager(config.MASTER_PASSWORD)
acc_manager = AccountManager("storage/sessions.json", crypto_manager)

def print_header():
    console.print(Panel(
        "[bold cyan]TG Star Sniper Sustainable - Phase 1[/bold cyan]\n"
        "[green]الأنظمة تعمل بكفاءة... (Stealth Mode: ON)[/green]\n"
        "[dim]Enterprise-Grade Architecture[/dim]",
        title="🎯 System Core", border_style="cyan", subtitle="v1.0"
    ))

async def async_add_account(name: str, api_id: int, api_hash: str, phone: str, proxy: dict = None):
    try:
        console.print("[yellow]جاري الاتصال بسيرفرات تلجرام (يتم تطبيق Stealth Rules)...[/yellow]")
        client = await acc_manager.add_account_step1(name, api_id, api_hash, phone, proxy)
        
        if not await client.is_user_authorized():
            code = Prompt.ask("[bold magenta]أدخل الكود المرسل إلى هاتفك/تلجرام[/bold magenta]")
            try:
                await client.sign_in(phone, code)
            except Exception as e:
                console.print(f"[bold red]خطأ أثناء تسجيل الدخول: {e}[/bold red]")
                return

        await acc_manager.save_client_session(client, name, api_id, api_hash, phone, proxy)
        console.print("[bold green]✓ تم تسجيل الحساب بنجاح وتم تشفير الجلسة وحفظها![/bold green]")
    except Exception as e:
        console.print(f"[bold red]فشلت عملية إضافة الحساب: {str(e)}[/bold red]")


@app.command()
def menu():
    print_header()
    while True:
        console.print("\n[bold yellow]=== القائمة الرئيسية (Main Menu) ===[/bold yellow]")
        table = Table(show_header=False, box=None)
        table.add_row("1.", "[green]إضافة حساب جديد[/green]", "(Add Account & Proxy)")
        table.add_row("2.", "[blue]عرض الحسابات[/blue]", "(List Accounts)")
        table.add_row("3.", "[magenta]إعداد حساب المستودع[/magenta]", "(Setup Vault)")
        table.add_row("4.", "[cyan]اعدادات التأخير الذكي[/cyan]", "(Stealth Engine Config)")
        table.add_row("5.", "[red]خروج[/red]", "(Exit)")
        console.print(table)
        
        choice = Prompt.ask("\n[bold cyan]اختر من القائمة رقماً[/bold cyan]", choices=["1", "2", "3", "4", "5"])
        
        if choice == "1":
            console.print("\n[bold yellow]-- إضافة حساب جديد --[/bold yellow]")
            name = Prompt.ask("أدخل اسم مميز للحساب (Account Name)")
            api_id_str = Prompt.ask("أدخل API ID")
            api_hash = Prompt.ask("أدخل API HASH")
            phone = Prompt.ask("أدخل رقم الهاتف مع رمز الدولة (مثال: +123456789)")
            
            use_proxy = Prompt.ask("هل ترغب في استخدام بروكسي لهذا الحساب؟ (y/n)", choices=["y", "n"])
            proxy_dict = None
            if use_proxy == 'y':
                p_type = Prompt.ask("نوع البروكسي (socks5/http)", default="socks5")
                p_ip = Prompt.ask("IP البروكسي")
                p_port = int(Prompt.ask("البورت (Port)"))
                proxy_dict = {"proxy_type": p_type, "addr": p_ip, "port": p_port}
            
            asyncio.run(async_add_account(name, int(api_id_str), api_hash, phone, proxy_dict))
            
        elif choice == "2":
            accounts = acc_manager.accounts
            if not accounts:
                console.print("\n[red]لا توجد حسابات مسجلة حالياً في النظام.[/red]")
            else:
                console.print("\n[bold blue]-- الحسابات المسجلة --[/bold blue]")
                for name, data in accounts.items():
                    vault_tag = "[bold yellow](Vault)[/bold yellow]" if data.get('is_vault') else ""
                    proxy_tag = "[green](Proxy Enabled)[/green]" if data.get('proxy') else ""
                    console.print(f"• [bold white]{name}[/bold white] - {data['phone']} {vault_tag} {proxy_tag}")

        elif choice == "3":
            accounts = [name for name in acc_manager.accounts.keys()]
            if not accounts:
                console.print("[red]الرجاء إضافة حسابات أولاً قبل تحديد الـ Vault.[/red]")
                continue
            
            vault_target = Prompt.ask("اختر الحساب ليكون المستودع (Vault)", choices=accounts)
            if acc_manager.set_vault_account(vault_target):
                console.print(f"[bold green]تم تعيين '{vault_target}' كحساب مستودع لكافة الغنائم![/bold green]")
        
        elif choice == "4":
             console.print("\n[yellow]قريباً في Phase 2 (تكوين التوزيع الطبيعي وبواسون للتأخيرات)..[/yellow]")

        elif choice == "5":
            console.print("\n[bold red]تم الإغلاق.. حافظ على استدامة النظام. وداعاً![/bold red]")
            break

if __name__ == "__main__":
    app()
