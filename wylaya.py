city =['Adrar' ,"Chlef", "Laghouat  ",
                                            "Oum El Bouaghi ",
                                            "Batna ",  
                                            "Bejaia",
                                            "Biskra",   
                                            "Bechar",
                                            "Blida ",  
                                            "Bouira",   
                                            "Tamanrasset",     
                                            "Tebessa ",            
                                            "Tlemcen ",                            
                                            "Tiaret  ",                     
                                            "Tizi Ouzou  ",          
                                            "Algiers ",                                    
                                            "Djelfa  ",                     
                                            "Jijel   ",       
                                            "Setif   ",               
                                            "Saida   ",           
                                            "Skikda  ",         
                                            "Sidi Bel Abbes ",     
                                            "Annaba  ",             
                                            "Guelma  ",             
                                            "Constantine ",                              
                                            "Medea",              
                                            "Mostaganem  ",        
                                            "MSila",             
                                            "Mascara     ",              
                                            "Ouargla     ",                      
                                            "Oran ",                             
                                            "El Bayadh   ",                     
                                            "Illizi             ",                         
                                            "Bordj Bou Arreridj ",                    
                                            "Boumerdes     ",                         
                                            "El Tarf       ",                                  
                                            "Tindouf       ",                                      
                                            "Tissemsilt    ",                        
                                            "El Oued       ",                                  
                                            "Khenchela     ",                         
                                            "Souk Ahras    ",                                
                                            "Tipaza        ",                                     
                                            "Mila          ",                                 
                                            "Ain Defla     ",                                     
                                            "Naama         ",                                          
                                            "Ain Temouchent",                                                 
                                            "Ghardaia      ",                                   
                                            "Relizane      ",                           
                                            "El MGhair     ",                                    
                                            "El Menia      ",                             
                                            "Ouled Djellal ",                                     
                                            "Bordj Baji Mokhtar ",                                         
                                            "Beni Abbes         ",                    
                                            "Timimoun           ",                           
                                            "Touggourt          ",                             
                                            "Djanet             ",                                      
                                            "In Salah           ",                       
                                            "In Guezzam         " ]   

i=0 
f = open("city.txt", "w")
for c  in city :
    i=i+1
    t='<option value="%s">%d-%s</option> \n'% (c,i, c)
    f.write(t)
f.close()