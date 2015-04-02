
def effectiveness(drug_rate, sensitivity,specificity):
    '''prob_drug_positive = p_drug * p_positve_drug / p_postive 
       p_postive 
         = positve when drug + false postive { P(postive|no drug)}
         = p_drug * p_postive_drug + (1- specificity )*(1-p_drug) 

       high specificity will reduce the value of denominator,hence increase the 
       effectiveness
       especially, when drug_rate is low, the false sensitive must be very small to 
       improve the effectiveness 

       while if improve the sensitivity itself, because both the numerator and 
       denominator are increased, the effectiveness doesn't change much.
    '''
    return drug_rate * sensitivity / \
            (sensitivity*drug_rate + (1- specificity )*(1- drug_rate))

def main():
    drug_rate = [0.05, 0.01]
    sensitivity, specificity = 0.60, 0.99
    for d in drug_rate:
        print 'drug rate:%4.2f%%, effectiveness: %4.2f%%' % \
              (d*100, effectiveness(d,sensitivity,specificity)*100)

if __name__ == '__main__':
    main()