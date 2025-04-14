def find_cab():
    for ab in range(10, 100):       
        cab = ab * ab    
        if 100 <= cab <= 999:          
            ab_str = str(ab)
            cab_str = str(cab)            
            if cab_str[0] == ab_str[0]:                
                return cab
    return None
result = find_cab()
print(result)
