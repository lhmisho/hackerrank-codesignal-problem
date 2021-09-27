// https://app.codesignal.com/challenge/ENTkv7rJ3TxdNPoeo
import (
	"strings"
)

func domainType(domains []string) []string {
	var domainsLen int = len(domains)
	var domainTypes []string
	if domainsLen >= 4 && domainsLen <= 25 {
		for i := 0; i < domainsLen; i++ {
			domLen := len(domains[i])
			if domLen >= 5 && domLen <= 20 {
				domainArr := strings.Split(domains[i], ".")
				dom := len(domainArr) - 1
				fmt.Println(domainArr[dom])
				if domainArr[dom] == "com" {
					domainTypes = append(domainTypes, "commercial")
				} else if domainArr[dom] == "org" {
					domainTypes = append(domainTypes, "organization")
				} else if domainArr[dom] == "net" {
					domainTypes = append(domainTypes, "network")
				} else if domainArr[dom] == "info" {
					domainTypes = append(domainTypes, "information")
				}
			}
		}
	}
	return domainTypes
}
