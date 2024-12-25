class Solution(object):
    def reverseOnlyLetters(self, s):
        l, r = 0, len(s) - 1  # İki pointer
        s = list(s)  # Stringi listeye çevirdik
        while l < r:  # Pointerlar buluşana kadar çalışır
            if not s[l].isalpha():  # Sol pointer harf değilse atla
                l += 1
            elif not s[r].isalpha():  # Sağ pointer harf değilse atla
                r -= 1
            else:  # Her iki pointer da harfse yer değiştir ve pointerları ilerlet
                s[l], s[r] = s[r], s[l]
                l += 1 
                r -= 1
        return ''.join(s)  # Listeyi tekrar string'e çevirip döndür
