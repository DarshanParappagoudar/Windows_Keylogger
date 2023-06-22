import subprocess


def check_for_keylogger():
    """
    This function checks the system processes and services for known keylogging malware.
    """
    # Set of common keylogging process names
    keylogger_processes = {"svchost.exe", "winlogon.exe", "wininit.exe", "explorer.exe", "ctfmon.exe", "dwm.exe",
                           "taskhost.exe", "logonui.exe", "conhost.exe", "spoolsv.exe", "wsc_proxy.exe", "nvtray.exe",
                           "mobsync.exe", "System Idle Process"}

    # Check running processes for keylogger process names
    processes = subprocess.run('tasklist', capture_output=True, text=True).stdout.split('\n')
    process_warnings = []
    for process in processes:
        if any(name in process for name in keylogger_processes):
            process_warnings.append(process)

    if process_warnings:
        print("Keylogger Processes Found:")
        for process in process_warnings:
            print(f"WARNING: {process} may be a keylogger.")
        print()
    else:
        print("No keylogger processes found.")
        print()

    # Set of keylogger service names
    keylogger_services = {"SSFK.sys", "hookdump.sys", "i8042prt.sys", "kbdclass.sys", "mouclass.sys", "msio64.sys",
                          "kprocesshacker.sys", "winring0x64.sys", "api_log.dll", "injdrv.sys", "InjLib.dll",
                          "aswKbd.sys", "Atiesrxx.exe", "Ati2evxx.exe", "Ati2evxx.dll", "LVPrcSrv.exe", "LVPrcS64.exe",
                          "LogiRegistryService.exe", "LMouFilt.Sys", "LHidFilt.Sys", "LMouKE.Sys", "LHidKE.Sys",
                          "npggsvc.exe", "amfipspi32.dll", "wdica.sys", "hidusbfx2.sys",
                          "Enigma Virtual Box Driver.sys", "pehook.sys", "pe386.sys", "shl_hook.dll", "mf.sys",
                          "ctldrvins.exe", "intelhaxm.sys", "atkwmiacpi64.sys", "btath_hcrp.sys", "btath_rcp.sys",
                          "sptd.sys", "sptd2.sys", "ElbyCDIO.sys", "ElbyDelay.sys", "pfc.sys", "PdiDrv.sys",
                          "SysPlant.sys", "Trufos.sys", "x10ufx2.sys", "x10uf32.dll", "UltraMonUtility.sys",
                          "BCMWLTRY.EXE", "FNetMon.sys", "Rtenic64.sys"}

    # Check running services for keylogger service names
    services = subprocess.run('net start', capture_output=True, text=True).stdout.split('\n')
    service_warnings = []
    for service in services:
        if any(name in service for name in keylogger_services):
            service_warnings.append(service)

    if service_warnings:
        print("Keylogger Services Found:")
        for service in service_warnings:
            print(f"WARNING: {service} may be a keylogger.")
        print()
    else:
        print("No keylogger services found.")
        print()


check_for_keylogger()
