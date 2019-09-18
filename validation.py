

def IsInterfaceUp2(interfaceobj, ifname):
    #interfaceobj must be a json loads based object
    # show interface x/x | json
    #jstring = "interface_information[0].physical_interface[0].oper_status[0].data"
    jstring = "interface_information[0].physical_interface[0].oper_status[0].data"
    jstring2 = "interface_information[0].physical_interface[0].mtu[0].data"
    jstring3 = "interface_information[0].physical_interface[0].description[0].data"
    jstring4 = "interface_information[0].physical_interface[0].physicalAddress[0].data"


    interfaceobjsearch = jmespath.compile(jstring)
    interfaceobjsearch2 = jmespath.compile(jstring2)
    interfaceobjsearch3 = jmespath.compile(jstring3)
    interfaceobjsearch4 = jmespath.compile(jstring4)

    interfaceobj = interfaceobjsearch.search(interfaceobj)
    interfaceobj2 = interfaceobjsearch2.search(interfaceobj)
    interfaceobj3 = interfaceobjsearch3.search(interfaceobj)
    interfaceobj4 = interfaceobjsearch4.search(interfaceobj)

    print("checking an interface up status..")
    #if debugsession:
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()

    intf = ifname
    #if debug:
    #    print(intf)
    try:
        #if debug:
            #print(interfaceobj)

        if interfaceobj == u"up":

            return "PASS - " + "Interface: " + ifname + " is UP ... \nMTU: " \
                   + str(interfaceobj2) + "\nDescription: " \
                   + str(interfaceobj3) \
                   + "\nphysicalAddress: " + str(interfaceobj4)
        else:
            raise ValueError("interface down: " + str(ifname))
    except:
        raise  ValueError("unknown error in aristavalidator.IsInterfaceUp")
