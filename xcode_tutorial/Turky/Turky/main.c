//
//  main.c
//  Turky
//
//  Created by Bo Dong on 08/08/2017.
//  Copyright © 2017 Bo Dong. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    float   weight=14.2;
    printf("The turky weights %f .\n", weight);
    
    float cookingTime;
    cookingTime = 15.0+15.0*weight;
    printf("Cook it for %f minutes. \n", cookingTime);
    return 0;
}
