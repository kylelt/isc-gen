# isc-gen
Convert to isc-dhcp subnets

## Take an excel table and generate the repetitive parts of isc-dhcp config file(s)

### TODO
- Ignore /32 Network entries they are guaranteed apart of another network,
  - Should generate host stubs

### Done
- Spread subnets into their group (files ), done
- Add failover for pools, done
- Remove absolute path done
