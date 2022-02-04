def main():
    # https://stackoverflow.com/questions/7561498/python-3-gives-wrong-output-when-dividing-two-large-numbers
    # ponieważ dzielenie gwarantowane było że będzie całkowite to można było użyć //
    # python przy dużych liczbach i ich dzieleniu może dawać jakieś błędy
    
    ilosc_linijek_kodu = int(input())
        
    mini = (ilosc_linijek_kodu * 12) // 10
    maxi = (2 * ilosc_linijek_kodu) * 2
    
    print(int(mini), end = " ")
    print(int(maxi))
    
main()