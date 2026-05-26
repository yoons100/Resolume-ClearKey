![Platform](https://img.shields.io/badge/platform-Windows-blue) [![Release](https://img.shields.io/badge/Release-V1.0-fc1ba6)](https://github.com/yoons100/Resolume-ClearKey/releases) ![License](https://img.shields.io/github/license/yoons100/Resolume-ClearKey)

## Resolume Clear Hotkey V1.0

ResolumeClearHotkey is a simple system tray App that assigns the **Ctrl + Delete** shortcut to clear selected clips in Resolume.  
  

<img width="192" height="67" alt="h1" src="https://github.com/user-attachments/assets/ad12eb51-c3a5-4f00-a3eb-c334d80768d4" />  
  

<img width="184" height="54" alt="h2" src="https://github.com/user-attachments/assets/755d04ed-9982-4532-b541-7a5ae2e6e904" />

### How to Use

1. Launch the App.
   - A gray DEL icon will appear in the Windows system tray.

2. Start Resolume.
   - The tray icon will turn green when the App successfully connects to the Resolume API.

3. Select one or more clips in Resolume.

4. Press **Ctrl + Delete**.
   - The selected clips will be cleared automatically.

### Notes

#### 1. Resolume API Configuration Required

This App uses the Resolume REST API.

In Resolume, open:

**Preferences → Webserver**

Enable the Webserver and configure:

- Listen Port: **8880 ~ 8889**
- Listen Address: **127.0.0.1**

<img width="462" height="352" alt="h3" src="https://github.com/user-attachments/assets/79de3a0b-515a-43c2-b706-25bbfc2455cc" />


#### 2. Sequential Deletion

Selected clips are cleared one by one through the API.

For this reason, **Undo (Ctrl + Z)** is also applied sequentially and must be pressed multiple times to restore multiple deleted clips.

#### 3. Shortcut Works Only When Connected

The hotkey is enabled only when the App is successfully connected to the Resolume API.

For convenience, it is recommended to add ResolumeClearHotkey to the Windows Startup folder.

#### 4. Keep the Tray Icon Visible

Keeping the tray icon visible makes it easy to check the connection status.

Windows Settings:

**Taskbar Settings → Other System Tray Icons → Enable "ResolumeClearHotkey"**

### Tray Icon Status

- Gray icon: Not connected
- Green icon: Connected to Resolume API

---

## Resolume ClearHotkey V1.0

ResolumeClearHotkey는 Resolume에서 클립 삭제(Clear)를 **Ctrl + Delete** 단축키로 실행할 수 있도록 해주는 간단한 시스템 트레이 앱입니다.
  

<img width="192" height="67" alt="h1" src="https://github.com/user-attachments/assets/ad12eb51-c3a5-4f00-a3eb-c334d80768d4" />  
  

<img width="184" height="54" alt="h2" src="https://github.com/user-attachments/assets/755d04ed-9982-4532-b541-7a5ae2e6e904" />

### 사용방법

1. 앱을 실행합니다.
   - Windows 시스템 트레이에 회색 DEL 아이콘이 표시됩니다.

2. Resolume을 실행합니다.
   - Resolume API와 연결되면 트레이 아이콘이 녹색으로 변경됩니다.

3. 삭제할 클립을 1개 또는 여러 개 선택합니다.

4. **Ctrl + Delete** 단축키를 누릅니다.
   - 선택된 클립이 자동으로 삭제됩니다.

### 참고사항

#### 1. Resolume API 설정 필요

이 앱은 Resolume REST API를 사용합니다.

Resolume에서 다음 메뉴를 열어 설정해 주세요.

**설정(Preferences) → Webserver**

다음과 같이 설정합니다.

- Listen Port : **8880 ~ 8889**
- Listen Address : **127.0.0.1**

<img width="462" height="352" alt="h3" src="https://github.com/user-attachments/assets/79de3a0b-515a-43c2-b706-25bbfc2455cc" />

#### 2. 순차 삭제 방식

선택된 클립은 API를 통해 하나씩 순차적으로 삭제됩니다.

따라서 **되돌리기(Ctrl + Z)** 역시 순차적으로 적용되며, 여러 개의 클립을 복구하려면 Ctrl + Z를 여러 번 눌러야 합니다.

#### 3. API 연결 시에만 단축키 동작

Resolume API와 연결된 상태에서만 단축키가 활성화됩니다.

편리하게 사용하려면 앱을 Windows 시작프로그램에 등록해 두는 것을 권장합니다.

#### 4. 시스템 트레이 아이콘 항상 표시 권장

시스템 트레이에 항상 표시되도록 설정하면 연결 상태를 쉽게 확인할 수 있습니다.

Windows 설정:

**작업 표시줄 설정 → 기타 시스템 트레이 아이콘 → ResolumeClearHotkey 켜기**

### 트레이 아이콘 상태

- 회색 아이콘 : 연결 안됨
- 녹색 아이콘 : Resolume API 연결됨

---
