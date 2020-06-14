import { Row,Col, Button, Select, Slider,notification } from "antd";
import { useEffect } from "react";
import React, {useState,useRef} from 'react';
import * as THREE from "three"
import OBJLoader from 'three-obj-loader';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import {graphql} from 'gatsby'
import Img from 'gatsby-image';

import DesignPicker from '../components/designpicker';
import ModelPicker  from '../components/modelpicker';
import GeometryInterpolator from "../utils/geometryInterpolator";



OBJLoader(THREE);


const {Option} = Select;

export default ({data}) => {
    let domRef;

    let humanGenerator = useRef(null);
    let shirtGenerator = useRef(null);
    let pantGenerator = useRef(null);
    let humanMin = useRef(null)
    let humanMax = useRef(null);
    let shirtMin = useRef(null)
    let shirtMax = useRef(null);
    let pantMin = useRef(null)
    let pantMax = useRef(null);


    let human = useRef(null);
    let shirt = useRef(null);
    let pant = useRef(null);

    


    let scene = useRef(null);



    const designs = data.designs.edges;
    //const models = data.models.edges;

    const [design,setDesign_] = useState(designs[0].node.childImageSharp.fluid.src);

    const setWaist=(w)=>{
        let newGeometry = humanGenerator.current.generateGeometry(w);
        human.current.children[0].geometry.attributes.position.array=Float32Array.from(newGeometry);
        human.current.children[0].geometry.attributes.position.needsUpdate = true;

        newGeometry = shirtGenerator.current.generateGeometry(w);
        shirt.current.children[0].geometry.attributes.position.array=Float32Array.from(newGeometry);
        shirt.current.children[0].geometry.attributes.position.needsUpdate = true;

        newGeometry = pantGenerator.current.generateGeometry(w);
        pant.current.children[0].geometry.attributes.position.array=Float32Array.from(newGeometry);
        pant.current.children[0].geometry.attributes.position.needsUpdate = true;
    }


    const setDesign = (design) => {
        setDesign_(design);
        const textureLoader = new THREE.TextureLoader();
        const material2 = new THREE.MeshPhongMaterial({map:textureLoader.load(design)})
        shirt.current.traverse( child => {
            if (child instanceof THREE.Mesh){
                child.material = material2;
                child.material.needsUpdate= true;
                child.material.map.needsUpdate = true;
                child.needsUpdate = true;
            }
        });
    }

    const setModel = (publicURL) => {
        if (human.current && scene.current) {scene.current.remove(human.current)}
        let loader= new THREE.OBJLoader();
        loader.load(
            publicURL, // Resource
            (object) => { // Once loaded.
                human.current = object;
                human.current.rotation.y = -Math.PI/2;
                console.log(scene.current,human.current);
                scene.current.add(human.current);
            },
            (xhr) => { //Updates
                console.log(( xhr.loaded / xhr.total * 100 ) + '% loaded');
            }

        );
    }
    
    useEffect( () => {
        let loader= new THREE.OBJLoader();

        // Make camera
        let near =0.1;
	    let far=10000;
        let fov=45;
        let radiusOfCamera=4;
        let heightOfCamera=1;
        let aspect = domRef.offsetWidth/domRef.offsetHeight;
        let camera = new THREE.PerspectiveCamera(fov,aspect,near,far);

        // Make Scene
        scene.current = new THREE.Scene();
        // Make renderer
        let renderer = new THREE.WebGLRenderer({ alpha: true });
        renderer.setClearColor( 0x99dd99, 1);

        let controls = new OrbitControls(camera,renderer.domElement);

        camera.position.z = radiusOfCamera;
        camera.position.y = heightOfCamera;

        renderer.setSize(domRef.offsetWidth, domRef.offsetHeight);
        domRef.appendChild(renderer.domElement);

        // Add a cube just because
        const geometry = new THREE.BoxGeometry();
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
        const cube = new THREE.Mesh(geometry, material);

    

        let animate = function () {
            requestAnimationFrame(animate);

            renderer.render(scene.current, camera);

        }
        animate();

        loader.load('/humans/woman/min/waistmin.obj',
        (object)=>{
            humanMin.current = object;
            human.current = humanMin.current;
            scene.current.add(human.current);

            loader.load('/humans/woman/max/waistmax.obj',
            (object2)=>{

                humanMax.current = object2

                humanGenerator.current = new GeometryInterpolator(humanMin.current,humanMax.current,10);


                let newGeometry = humanGenerator.current.generateGeometry(5);

                human.current.children[0].geometry.attributes.position.array=Float32Array.from(newGeometry);
                human.current.children[0].geometry.attributes.position.needsUpdate = true;

            });
           
        });


        loader.load('/humans/woman/min/shirtmin.obj',
            (object) => {
                shirtMin.current = object;
                shirt.current = shirtMin.current;

                const textureLoader = new THREE.TextureLoader();
                const material = new THREE.MeshBasicMaterial({map: textureLoader.load(design)});
                shirt.current.material = material;
                shirt.current.traverse( child => {
                    if (child instanceof THREE.Mesh){
                        child.material = material;
                        child.material.needsUpdate= true;
                        child.material.map.needsUpdate = true;
                        child.needsUpdate = true;
                    }
                });
                shirt.current.material.needsUpdate = true

                scene.current.add(shirt.current);

                loader.load('/humans/woman/max/shirtmax.obj',
                (object2) => {
                    shirtMax.current = object2;
                    shirtGenerator.current = new GeometryInterpolator(shirtMin.current,shirtMax.current,10);

                    console.log(shirtGenerator)


                    let newGeometry = shirtGenerator.current.generateGeometry(5);
                    shirt.current.children[0].geometry.attributes.position.array=Float32Array.from(newGeometry);
                    shirt.current.children[0].geometry.attributes.position.needsUpdate = true;
                })

        });

        loader.load('/humans/woman/min/bottomsmin.obj',
            (object) => {
                pantMin.current = object;
                pant.current = pantMin.current;

                const textureLoader = new THREE.TextureLoader();
                const material = new THREE.MeshBasicMaterial({map: textureLoader.load(designs[3].node.childImageSharp.fluid.src)});
                pant.current.material = material;
                pant.current.traverse( child => {
                    if (child instanceof THREE.Mesh){
                        child.material = material;
                        child.material.needsUpdate= true;
                        child.material.map.needsUpdate = true;
                        child.needsUpdate = true;
                    }
                });
                pant.current.material.needsUpdate = true

                scene.current.add(pant.current);

                loader.load('/humans/woman/max/bottomsmax.obj',
                (object2) => {
                    pantMax.current = object2;
                    pantGenerator.current = new GeometryInterpolator(pantMin.current,pantMax.current,10);

                    console.log(pantGenerator)


                    let newGeometry = pantGenerator.current.generateGeometry(5);
                    pant.current.children[0].geometry.attributes.position.array=Float32Array.from(newGeometry);
                    pant.current.children[0].geometry.attributes.position.needsUpdate = true;
                })

        });

        

        /*loader.load('/clothes/girl_shirt.obj',
            (object) => {
                console.log("Got shirt!")
                shirt.current = object;
                const textureLoader = new THREE.TextureLoader();
                const material2 = new THREE.MeshPhongMaterial({map:textureLoader.load(design)})
                shirt.current.traverse( child => {
                    if (child instanceof THREE.Mesh){
                        child.material = material2;
                    }
                });
                //shirt.position.z += 5;
                shirt.current.position.y += 0.143;
                //shirt.scale.set(0.006,0.006,0.006);
                scene.current.add(shirt.current);
            },
            (xhr) => {
                console.log("Shirt: ",xhr.loaded/xhr.total*100 ,"% Loaded")
            }
        )

        loader.load(
            '/humans/girl.obj', // Resource
            (object) => { // Once loaded.
                human.current = object;
                //human.rotation.y = -Math.PI/2;
                human.current.position.y -= 1
                const mat = new THREE.MeshPhongMaterial({color:0xFFDBAC})
                human.current.traverse(child => {
                    if (child instanceof THREE.Mesh){
                        child.material = mat;
                    }
                })
                scene.current.add(human.current);
            },
            (xhr) => { //Updates
                console.log(( xhr.loaded / xhr.total * 100 ) + '% loaded');
            }

        );*/


        //we need some light
        {
            const color =0xffffff;
            const intensity=0;
            const light  = new THREE.DirectionalLight(color,intensity)
            light.position.set(0,10,0);
            light.target.position.set(-5,0,0)
            scene.current.add(light);
            scene.current.add(light.target)
        }

        // hemisphere light
        {
            const skyColor = 0xB1E1FF;  // light blue
            const groundColor =  0x999999//0xB97A20;  // brownish orange
            const intensity = 1;
            const light = new THREE.HemisphereLight(skyColor, groundColor, intensity);
            scene.current.add(light);
        }

        window.addEventListener("resize",() => {
            if (domRef){
                camera.aspect = domRef.offsetWidth / domRef.offsetHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(domRef.offsetWidth, domRef.offsetHeight);
            }
        })

        

    },[]);

    return (
        <div style={{height:"100vh"}}>
            <Row style={{height:"100vh"}}>
                <Col xs={0} md={6} xl={5}>
                    <DesignPicker designs={designs} designState={[design,setDesign]}/>

                    
                </Col>
                <Col xs={24} md={12} xl={14} style={{borderLeft:"1px black solid",borderRight:"1px black solid"}}>
                    <div ref={ref => {domRef = ref}} style={{height:"100vh",width:"100%"}}>
                    </div>
                </Col>
                <Col xs={0} md={6} xl={5}>
                    <ModelPicker models={[]} modelState={{setModel}} setWaist={setWaist}/>
                    
                </Col>
            </Row>
        </div>
    )
}

export const Query = graphql`
query {
    designs : allFile (filter: {relativeDirectory: {eq: "images/designs"}}) {
        edges {
            node {
                childImageSharp {
                    fluid {
                    ...GatsbyImageSharpFluid
                    }
                }
            }
        }
    }
}`