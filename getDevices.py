import win32pdh
import win32security

print("==========================")
print("Listing des 'Devices' accessibles par l'utilisateur courant")
print("==========================")

# We get the list of device instances
handles, names = win32pdh.EnumObjectItems(None, None, "Device", win32pdh.PERF_DETAIL_WIZARD)

# We loop for all instances
for i in range(len(names)):
    name = names[i]
    handle = handles[i]

    # The last parameter corresponds to the information that we want to get
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

