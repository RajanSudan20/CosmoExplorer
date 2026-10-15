import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CosmoExplorer - 3D Space Simulator", page_icon="🚀", layout="wide")

st.title("🌌 CosmoExplorer: High-Graphics 3D Space Simulator")
st.markdown("Powered by WebGL & Three.js — Real-time celestial mechanics simulation inspired by high-end space games.")

# Three.js High-Graphics Space Simulator HTML/JS Component embedded in Streamlit
space_simulation_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body { margin: 0; background-color: #000; overflow: hidden; font-family: sans-serif; }
        #info { 
            position: absolute; top: 15px; left: 15px; color: #00ffcc; 
            background: rgba(0, 0, 0, 0.8); padding: 12px 18px; 
            border-radius: 8px; border: 1px solid #00ffcc; pointer-events: none;
            font-size: 14px; text-shadow: 0 0 5px #00ffcc;
        }
    </style>
</head>
<body>
    <div id="info">🚀 <b>Simulator Active</b><br/>Mouse click & drag karke space ko rotate karein!</div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Scene, Camera, Renderer setup
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight - 120);
        document.body.appendChild(renderer.domElement);

        // Lighting for 3D realism
        const ambientLight = new THREE.AmbientLight(0x222222);
        scene.add(ambientLight);
        
        const sunLight = new THREE.PointLight(0xffffff, 2.5, 400);
        scene.add(sunLight);

        // Realistic Starfield Background Particle System
        const starsGeometry = new THREE.BufferGeometry();
        const starsCount = 4000;
        const starPositions = new Float32Array(starsCount * 3);
        
        for(let i = 0; i < starsCount * 3; i++) {
            starPositions[i] = (Math.random() - 0.5) * 600;
        }
        
        starsGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
        const starsMaterial = new THREE.PointsMaterial({ color: 0xffffff, size: 0.8 });
        const starField = new THREE.Points(starsGeometry, starsMaterial);
        scene.add(starField);

        // Sun (Glowing Center Star)
        const sunGeo = new THREE.SphereGeometry(6, 32, 32);
        const sunMat = new THREE.MeshBasicMaterial({ color: 0xffcc00 });
        const sun = new THREE.Mesh(sunGeo, sunMat);
        scene.add(sun);

        // Planets Orbit System
        const planets = [];
        function createPlanet(radius, distance, color, speed, ring = false) {
            const orbitGroup = new THREE.Group();
            scene.add(orbitGroup);
            
            const geom = new THREE.SphereGeometry(radius, 32, 32);
            const mat = new THREE.MeshStandardMaterial({ color: color, roughness: 0.5 });
            const mesh = new THREE.Mesh(geom, mat);
            mesh.position.x = distance;
            orbitGroup.add(mesh);

            // Add rings for Saturn-like appearance
            if(ring) {
                const ringGeo = new THREE.RingGeometry(radius + 1, radius + 2.5, 32);
                const ringMat = new THREE.MeshBasicMaterial({ color: 0xaaaaaa, side: THREE.DoubleSide, transparent: true, opacity: 0.6 });
                const ringMesh = new THREE.Mesh(ringGeo, ringMat);
                ringMesh.rotation.x = Math.PI / 2;
                mesh.add(ringMesh);
            }
            
            planets.push({ group: orbitGroup, mesh: mesh, speed: speed });
        }

        // Creating Solar System Bodies (Mercury, Venus, Earth, Mars, Jupiter, Saturn)
        createPlanet(0.8, 12, 0xaaaaaa, 0.025); // Mercury
        createPlanet(1.4, 18, 0xe3bb76, 0.018); // Venus
        createPlanet(1.6, 26, 0x2277ff, 0.012); // Earth
        createPlanet(1.2, 35, 0xcc4400, 0.009); // Mars
        createPlanet(3.8, 50, 0xd4a373, 0.005); // Jupiter
        createPlanet(3.0, 68, 0xf4e2bb, 0.003, true); // Saturn with Rings

        camera.position.z = 80;
        camera.position.y = 25;
        camera.lookAt(0, 0, 0);

        // Interactive Mouse Controls for 3D Camera Rotation
        let isDragging = false;
        let previousMousePosition = { x: 0, y: 0 };

        window.addEventListener('mousedown', (e) => { isDragging = true; });
        window.addEventListener('mouseup', (e) => { isDragging = false; });
        window.addEventListener('mousemove', (e) => {
            if (isDragging) {
                const deltaX = e.clientX - previousMousePosition.x;
                const deltaY = e.clientY - previousMousePosition.y;
                scene.rotation.y += deltaX * 0.005;
                scene.rotation.x += deltaY * 0.005;
            }
            previousMousePosition = { x: e.clientX, y: e.clientY };
        });

        // Smooth Game-like Animation Loop
        function animate() {
            requestAnimationFrame(animate);
            
            // Orbit rotation & self rotation
            planets.forEach(p => {
                p.group.rotation.y += p.speed;
                p.mesh.rotation.y += 0.02;
            });
            
            starField.rotation.y += 0.0003;
            renderer.render(scene, camera);
        }
        animate();

        // Responsive Resizing
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / (window.innerHeight - 120);
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight - 120);
        });
    </script>
</body>
</html>
"""

components.html(space_simulation_html, height=700)
