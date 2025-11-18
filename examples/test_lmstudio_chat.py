import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# print(generate_random_string(10))  # генерирует случайную строку из 10 символов

# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
# base_url="http://localhost:1234/v1"
server_url = "http://localhost:1234/v1"  
# client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
client = OpenAI(base_url=server_url,api_key=generate_random_string(10))

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "Ты технический писатель. Пиши только на русском языке. Описывай только суть."},
    {"role": "user", "content": """
     Пожалуйста, напишите отформатированное .md сообщение на русском языке для git commit, используя результат команды git diff: 
     ```
     diff --git a/RedMaster/RedMaster/Properties/AssemblyInfo.cs b/RedMaster/RedMaster/Properties/AssemblyInfo.cs index 3cc3d36..f891f61 100644 --- a/RedMaster/RedMaster/Properties/AssemblyInfo.cs +++ b/RedMaster/RedMaster/Properties/AssemblyInfo.cs @@ -51,8 +51,8 @@ using System.Windows; // You can specify all the values or you can default the Build and Revision Numbers // by using the '*' as shown below: // [assembly: AssemblyVersion("1.0.*")] -[assembly: AssemblyVersion("4.1.0.1")] -[assembly: AssemblyFileVersion("4.1.0.1")] +[assembly: AssemblyVersion("4.1.0.2")] +[assembly: AssemblyFileVersion("4.1.0.2")] [assembly: NeutralResourcesLanguage("ru-RU")] [assembly: InternalsVisibleTo("RedMaster.IntegrationTests")] diff --git a/RedMaster/RedMaster/RedMaster.csproj b/RedMaster/RedMaster/RedMaster.csproj index 592ce3e..c8ed23e 100644 --- a/RedMaster/RedMaster/RedMaster.csproj +++ b/RedMaster/RedMaster/RedMaster.csproj @@ -35,7 +35,7 @@ <PublisherName>Газпром проектирование</PublisherName> <WebPage>publish.htm</WebPage> <AutorunEnabled>true</AutorunEnabled> - <ApplicationRevision>1</ApplicationRevision> + <ApplicationRevision>2</ApplicationRevision> <ApplicationVersion>4.1.0.%2a</ApplicationVersion> <UseApplicationTrust>false</UseApplicationTrust> <CreateDesktopShortcut>true</CreateDesktopShortcut> @@ -398,13 +398,13 @@ <Version>6.0.0</Version> </PackageReference> <PackageReference Include="tdmstools"> - <Version>2.24.0</Version> + <Version>2.25.0.2</Version> </PackageReference> <PackageReference Include="TdmsTools.Adapters.COMAPI"> <Version>3.4.0.1</Version> </PackageReference> <PackageReference Include="tdmstools.ComProvider"> - <Version>1.1.0</Version> + <Version>1.2.0.1</Version> </PackageReference> <PackageReference Include="TdmsTools.Sapper"> <Version>2.2.2</Version> diff --git a/RedMaster/RedMaster/ViewModels/MainWindowViewModel.cs b/RedMaster/RedMaster/ViewModels/MainWindowViewModel.cs index c1eb44a..50db469 100644 --- a/RedMaster/RedMaster/ViewModels/MainWindowViewModel.cs +++ b/RedMaster/RedMaster/ViewModels/MainWindowViewModel.cs @@ -38,7 +38,7 @@ namespace RedMaster.ViewModels _notificationInteractionRequest = new InteractionRequest<INotification>(); _ = _regionManager.RegisterViewWithRegion("WizardRegion", typeof(WelcomeView)); - _title = $"{CommonConstants.PROGRAMM_TITLE} (TDMS {TdmsWorker.AppVersion})"; + _title = $"{CommonConstants.PROGRAMM_TITLE} (TDMS {TdmsWorker.ClientVersion})"; } #endregion
     ```
     в после описания добавь ссылку на задачу #1984
     
     используй шаблон вывода:
     
     ```
     {Краткий заголовок}

     {Описание изменений}

     {Ссылка на задачу}
     ```
    
    """}
  ],
  temperature = 0.5,
  # max_tokens = 100,
  stream = False
)

# history = completion.choices[0].message
# Uncomment to see chat history
import json
gray_color = "\033[90m"
reset_color = "\033[0m"
# print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
# print(json.dumps(history, indent=2))

print(completion.choices[0].message)
print(f"\n{'-'*55}\n{reset_color}")


print(completion.choices[0].message.content)
