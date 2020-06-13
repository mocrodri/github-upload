"""
++ The goal is to get a standardized technique to flood RP mapping information (remember, Auto-RP is proprietary)

Goals of BSR :

    Get a standard to distribute RP mapping information
    Do NOT use multicast to distribute information. Instead, informations are propagated hop by hop, like Spanning Tree BPDU. This tackles one of the big drawback of Auto-RP which is the need to use dense-mode or static RP for the 2 Auto-RP groups.
    Provide more flexibility in RP election. With Auto-RP, if there are 2 candidates RPs for the same set of groups, only one is used (highest IP). BSR allows to use both of them by selecting RP based on a hash.
aaaa
bbbb
"""
