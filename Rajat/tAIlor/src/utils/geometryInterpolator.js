import {linearRegression} from 'simple-statistics';


export default class GeometryInterpolator{
    constructor(objMin,objMax,breaks){
        this.regressionArray = [];
        let tempArr = [];

        let arrayMax=objMax.children[0].geometry.attributes.position.array
        let arrayMin=objMin.children[0].geometry.attributes.position.array

        for (let i=0;i<arrayMin.length;i++){
            tempArr.push([[1,arrayMin[i]],[breaks,arrayMax[i]]]);
        }

        for (let i =0;i<arrayMin.length;i++){
            this.regressionArray.push(linearRegression(tempArr[i]))
        }

    }

    generateGeometry(level){
        let newGeometry = [];

        for (let i=0;i<this.regressionArray.length;i++){
            // say the parameter is 2, then we need, y = mx+c, right? so 
            let y = this.regressionArray[i].m *level + this.regressionArray[i].b;
            newGeometry.push(y)
        }
        return newGeometry;
    }
}