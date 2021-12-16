import win32pdh
import win32security

print("==========================")
print("Listing des 'Devices' accessibles par l'utilisateur courant")
print("==========================")

print("Device n°",1,":","PC")

items, instances = win32pdh.EnumObjectItems(None, None, "Device", win32pdh.PERF_DETAIL_WIZARD)

for i in range(len(instances)):
    name = instances[i]
    handle = items[i]

    securityDescriptor_owner = win32security.GetKernelObjectSecurity(handle, 0)
    securityDescriptor_group = win32security.GetKernelObjectSecurity(handle, 1)
    securityDescriptor_dacl = win32security.GetKernelObjectSecurity(handle, 2)
    securityDescriptor_sacl = win32security.GetKernelObjectSecurity(handle, 3)

    print("Device n°", i, ":", name, "\n")
    print("- Handle:", handle)
    print("- Owner:", securityDescriptor_owner)
    print("- Group:", securityDescriptor_group)
    print("- DACL:", securityDescriptor_dacl)
    print("- SACL:", securityDescriptor_sacl)

    print("-------------")

