def letters(order,length)
    
    aa =(('   #    '),(' #   #  '),('#     # '),('####### '),('#     # '),('#     # '),('#     # '))
    bb =(('######  '),('#     # '),('#     # '),('######  '),('#     # '),('#     # '),('######  '))
    cc =((' #####  '),('#     # '),('#       '),('#       '),('#       '),('#     # '),(' #####  '))
    dd =(('######  '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),('######  '))
    ee =(('####### '),('#       '),('#       '),('######  '),('#       '),('#       '),('####### '))
    ff =(('####### '),('#       '),('#       '),('#####   '),('#       '),('#       '),('#       '))
    gg =((' #####  '),('#       '),('#       '),('#   ### '),('#     # '),('#    ## '),(' #### # '))
    hh =(('#     # '),('#     # '),('#     # '),('####### '),('#     # '),('#     # '),('#     # '))
    ii =((' #####  '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    '),(' #####  '))
    jj =(('  ##### '),('     #  '),('     #  '),('     #  '),('     #  '),(' #   #  '),('  ###   '))
    kk =(('#     # '),('#    #  '),('#   #   '),('####    '),('#   #   '),('#    #  '),('#     # '))
    ll =((' #      '),(' #      '),(' #      '),(' #      '),(' #      '),(' #      '),(' #####  '))
    mm =(('#     # '),('##   ## '),('# # # # '),('#  #  # '),('#     # '),('#     # '),('#     # ')) 
    nn =(('#     # '),('##    # '),('# #   # '),('#  #  # '),('#   # # '),('#    ## '),('#     # ')) 
    oo =((' #####  '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),(' #####  ')) 
    pp =(('######  '),('#     # '),('#     # '),('######  '),('#       '),('#       '),('#       ')) 
    qq =((' #####  '),('#     # '),('#     # '),('#     # '),('#   # # '),('#    #  '),(' #### # ')) 
    rr =(('######  '),('#     # '),('#     # '),('######  '),('#   #   '),('#    #  '),('#     # ')) 
    ss =((' ###### '),('#       '),('#       '),(' #####  '),('      # '),('      # '),('######  '))
    tt =(('####### '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    '),('   #    ')) 
    uu =(('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),('#     # '),(' #####  '))
    vv =(('#     # '),('#     # '),('#     # '),(' #   #  '),(' #   #  '),('  # #   '),('   #    '))
    ww =(('#     # '),('#     # '),('#  #  # '),('#  #  # '),('#  #  # '),('# # # # '),(' #   #  ')) 
    xx =(('#     # '),(' #   #  '),('  # #   '),('   #    '),('  # #   '),(' #   #  '),('#     # ')) 
    yy =(('#     # '),('#     # '),(' #   #  '),('  # #   '),('   #    '),('   #    '),('   #    '))
    zz =(('####### '),('     #  '),('    #   '),('   #    '),('  #     '),(' #      '),('####### '))
    em =(('        '),('        '),('        '),('        '),('        '),('        '),('        '))
    dictionary = {' ':em,'a':aa,'b':bb,'c':cc,'d':dd,'e':ee,'f':ff,'g':gg,'h':hh,'i':ii,'j':jj,'k':kk,'l':ll,'m':mm,'n':nn,'o':oo,'p':pp,'q':qq,'r':rr,'s':ss,'t':tt,'u':uu,'v':vv,'w':ww,'x':xx,'y':yy,'z':zz}
    screen = [' ']*7    
    for j in range(7):
        for i in range(length):
            screen[j] = screen[j] + dictionary[order[i]][j]
        print screen[j]    
    return screen    
    

def main():
    word = raw_input('please input any word:')
    length = len(word)
    letters(word,length)

main()
