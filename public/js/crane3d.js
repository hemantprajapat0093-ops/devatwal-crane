// Devatwal Crane Service - 3D Interactive Crane Simulation
// Powered by Three.js

let scene, camera, renderer, controls;
let craneGroup, cabinGroup, boomBase, boomExtend, hookGroup, cableLine, hazardLight;
let suspendedLoad;
let isDemoMode = true;
let animClock = 0;
let isCanvasVisible = true;
let animFrameId = null;
let isMobileDevice = false;

// Crane State variables
const craneState = {
  rotationY: 0,
  boomAngle: 0.35,      // radians
  boomExtension: 0.8,   // 0 to 2.5
  hookHeight: 2.0,     // distance below boom tip
  autoRotate: true,
};

function init3DCrane() {
  const container = document.getElementById('crane-3d-canvas-container');
  if (!container) return;

  isMobileDevice = window.innerWidth < 768 || ('ontouchstart' in window);
  const width = container.clientWidth || 360;
  const height = container.clientHeight || (isMobileDevice ? 420 : 520);

  // 1. Scene setup
  scene = new THREE.Scene();
  scene.background = null;

  // 2. Camera setup - wider perspective for expansive desktop display
  camera = new THREE.PerspectiveCamera(42, width / height, 0.1, 100);
  camera.position.set(13, 8, 14);

  // 3. Renderer setup - Optimized for Mobile 120Hz Smooth Scrolling
  renderer = new THREE.WebGLRenderer({ 
    antialias: !isMobileDevice, 
    alpha: true,
    powerPreference: isMobileDevice ? 'low-power' : 'high-performance'
  });
  renderer.setSize(width, height);
  renderer.setPixelRatio(isMobileDevice ? 1 : Math.min(window.devicePixelRatio || 1, 2));
  renderer.shadowMap.enabled = !isMobileDevice;
  if (!isMobileDevice) {
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  }
  renderer.domElement.style.touchAction = 'pan-y';
  container.innerHTML = '';
  container.appendChild(renderer.domElement);

  // 4. Orbit Controls - Touch gestures tuned to prevent vertical scroll hijacking
  if (typeof THREE.OrbitControls !== 'undefined') {
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.maxPolarAngle = Math.PI / 2 - 0.05;
    controls.minDistance = 6;
    controls.maxDistance = 26;
    controls.target.set(0, 2.5, 0);

    if (isMobileDevice) {
      controls.enableZoom = false;
      // Single finger touch scrolls page naturally; two fingers rotate crane
      controls.touches = {
        ONE: THREE.TOUCH.NONE,
        TWO: THREE.TOUCH.ROTATE
      };
    }
  }

  // 5. Lighting with high-tech blue/cyan accents
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.85);
  scene.add(ambientLight);

  const sunLight = new THREE.DirectionalLight(0xffffff, 1.4);
  sunLight.position.set(18, 28, 15);
  sunLight.castShadow = !isMobileDevice;
  if (!isMobileDevice) {
    sunLight.shadow.mapSize.width = 1024;
    sunLight.shadow.mapSize.height = 1024;
  }
  scene.add(sunLight);

  const fillLight = new THREE.DirectionalLight(0x38bdf8, 0.8);
  fillLight.position.set(-15, 12, -10);
  scene.add(fillLight);

  hazardLight = new THREE.PointLight(0x38bdf8, 2.5, 10);
  hazardLight.position.set(0, 4.2, 0);
  scene.add(hazardLight);

  // 6. Platform
  createGroundPlatform();

  // 7. Crane Assembly
  buildDevatwalCrane();

  // 8. Resize Listener
  window.addEventListener('resize', onWindowResize, { passive: true });

  // 9. Controls
  setupInteractiveControls();

  // 10. Viewport Intersection Observer (Auto-freezes WebGL loop when offscreen)
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const wasVisible = isCanvasVisible;
        isCanvasVisible = entry.isIntersecting;
        if (isCanvasVisible && !wasVisible && !animFrameId) {
          animate();
        }
      });
    }, { threshold: 0.05 });
    observer.observe(container);
  }

  // 11. Start Animation Loop
  animate();
}

function createGroundPlatform() {
  const floorGeo = new THREE.CylinderGeometry(9, 9, 0.3, 48);
  const floorMat = new THREE.MeshStandardMaterial({
    color: 0x0a1122,
    roughness: 0.85,
    metalness: 0.25,
  });
  const floor = new THREE.Mesh(floorGeo, floorMat);
  floor.position.y = -0.15;
  floor.receiveShadow = true;
  scene.add(floor);

  const ringGeo = new THREE.RingGeometry(8.6, 8.85, 48);
  const ringMat = new THREE.MeshBasicMaterial({
    color: 0x38bdf8,
    side: THREE.DoubleSide,
  });
  const ring = new THREE.Mesh(ringGeo, ringMat);
  ring.rotation.x = -Math.PI / 2;
  ring.position.y = 0.02;
  scene.add(ring);

  const grid = new THREE.GridHelper(18, 18, 0x38bdf8, 0x1e293b);
  grid.position.y = 0.01;
  scene.add(grid);
}

function buildDevatwalCrane() {
  craneGroup = new THREE.Group();
  scene.add(craneGroup);

  const craneYellow = new THREE.MeshStandardMaterial({
    color: 0xf59e0b,
    roughness: 0.35,
    metalness: 0.25,
  });
  const chassisDark = new THREE.MeshStandardMaterial({
    color: 0x0b1329,
    roughness: 0.6,
    metalness: 0.7,
  });
  const chromeSteel = new THREE.MeshStandardMaterial({
    color: 0xf8fafc,
    roughness: 0.2,
    metalness: 0.9,
  });
  const rubberBlack = new THREE.MeshStandardMaterial({
    color: 0x090d16,
    roughness: 0.9,
  });
  const cabinGlass = new THREE.MeshPhysicalMaterial({
    color: 0x38bdf8,
    transparent: true,
    opacity: 0.5,
    roughness: 0.1,
    transmission: 0.85,
    thickness: 0.5,
  });

  // Chassis
  const chassisGeo = new THREE.BoxGeometry(2.6, 0.75, 5.2);
  const chassis = new THREE.Mesh(chassisGeo, chassisDark);
  chassis.position.y = 1.1;
  chassis.castShadow = true;
  chassis.receiveShadow = true;
  craneGroup.add(chassis);

  // Counterweight
  const counterGeo = new THREE.BoxGeometry(2.5, 0.9, 1.4);
  const counterweight = new THREE.Mesh(counterGeo, craneYellow);
  counterweight.position.set(0, 1.3, -2.1);
  counterweight.castShadow = true;
  craneGroup.add(counterweight);

  // 4 Large Wheels
  const wheelPositions = [
    { x: -1.45, z: 1.6, r: 0.75, w: 0.5 },
    { x: 1.45, z: 1.6, r: 0.75, w: 0.5 },
    { x: -1.45, z: -1.7, r: 0.75, w: 0.5 },
    { x: 1.45, z: -1.7, r: 0.75, w: 0.5 },
  ];

  wheelPositions.forEach((pos) => {
    const wheelGroup = new THREE.Group();
    wheelGroup.position.set(pos.x, pos.r, pos.z);

    const tireGeo = new THREE.CylinderGeometry(pos.r, pos.r, pos.w, 24);
    const tire = new THREE.Mesh(tireGeo, rubberBlack);
    tire.rotation.z = Math.PI / 2;
    tire.castShadow = true;
    wheelGroup.add(tire);

    const rimGeo = new THREE.CylinderGeometry(pos.r * 0.55, pos.r * 0.55, pos.w + 0.02, 16);
    const rim = new THREE.Mesh(rimGeo, craneYellow);
    rim.rotation.z = Math.PI / 2;
    wheelGroup.add(rim);

    const capGeo = new THREE.CylinderGeometry(0.12, 0.12, pos.w + 0.05, 8);
    const cap = new THREE.Mesh(capGeo, chromeSteel);
    cap.rotation.z = Math.PI / 2;
    wheelGroup.add(cap);

    craneGroup.add(wheelGroup);
  });

  // Stabilizers
  [-1.3, 1.3].forEach((x) => {
    const outriggerGeo = new THREE.CylinderGeometry(0.1, 0.1, 0.8, 12);
    const outrigger = new THREE.Mesh(outriggerGeo, chassisDark);
    outrigger.position.set(x, 0.5, 2.5);
    craneGroup.add(outrigger);

    const padGeo = new THREE.CylinderGeometry(0.3, 0.3, 0.08, 16);
    const pad = new THREE.Mesh(padGeo, craneYellow);
    pad.position.set(x, 0.1, 2.5);
    craneGroup.add(pad);
  });

  // Cabin & Turntable
  cabinGroup = new THREE.Group();
  cabinGroup.position.set(0, 1.5, 0.2);
  craneGroup.add(cabinGroup);

  const slewGeo = new THREE.CylinderGeometry(0.9, 0.95, 0.25, 24);
  const slew = new THREE.Mesh(slewGeo, chassisDark);
  slew.position.set(0, 0.12, 0);
  cabinGroup.add(slew);

  const cabinBodyGeo = new THREE.BoxGeometry(1.2, 1.6, 1.7);
  const cabinBody = new THREE.Mesh(cabinBodyGeo, craneYellow);
  cabinBody.position.set(-0.65, 1.05, -0.1);
  cabinBody.castShadow = true;
  cabinGroup.add(cabinBody);

  const frontGlassGeo = new THREE.PlaneGeometry(1.0, 0.9);
  const frontGlass = new THREE.Mesh(frontGlassGeo, cabinGlass);
  frontGlass.position.set(-0.65, 1.25, 0.76);
  cabinGroup.add(frontGlass);

  const sideGlassGeo = new THREE.PlaneGeometry(1.2, 0.8);
  const sideGlass = new THREE.Mesh(sideGlassGeo, cabinGlass);
  sideGlass.rotation.y = -Math.PI / 2;
  sideGlass.position.set(-1.26, 1.25, -0.1);
  cabinGroup.add(sideGlass);

  // Window AC Unit
  const acUnitGeo = new THREE.BoxGeometry(0.45, 0.45, 0.7);
  const acUnitMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.4 });
  const acUnit = new THREE.Mesh(acUnitGeo, acUnitMat);
  acUnit.position.set(-1.3, 1.35, -0.5);
  acUnit.castShadow = true;
  cabinGroup.add(acUnit);

  // Roof Beacon
  const beaconDomeGeo = new THREE.SphereGeometry(0.12, 16, 12);
  const beaconDomeMat = new THREE.MeshStandardMaterial({
    color: 0x38bdf8,
    emissive: 0x0284c7,
    emissiveIntensity: 0.9,
  });
  const beaconDome = new THREE.Mesh(beaconDomeGeo, beaconDomeMat);
  beaconDome.position.set(-0.65, 1.95, -0.1);
  cabinGroup.add(beaconDome);

  const engineGeo = new THREE.BoxGeometry(1.0, 1.1, 2.2);
  const engine = new THREE.Mesh(engineGeo, craneYellow);
  engine.position.set(0.65, 0.8, -0.3);
  engine.castShadow = true;
  cabinGroup.add(engine);

  // Boom Assembly
  boomBase = new THREE.Group();
  boomBase.position.set(0.2, 1.2, -0.8);
  cabinGroup.add(boomBase);

  const bracketGeo = new THREE.BoxGeometry(0.7, 0.8, 0.8);
  const bracket = new THREE.Mesh(bracketGeo, chassisDark);
  boomBase.add(bracket);

  const boom1Geo = new THREE.BoxGeometry(0.6, 0.7, 4.6);
  const boom1 = new THREE.Mesh(boom1Geo, craneYellow);
  boom1.position.set(0, 0.2, 2.2);
  boom1.castShadow = true;
  boomBase.add(boom1);

  const cylCaseGeo = new THREE.CylinderGeometry(0.12, 0.14, 1.8, 12);
  const cylCase = new THREE.Mesh(cylCaseGeo, chassisDark);
  cylCase.rotation.x = Math.PI / 4;
  cylCase.position.set(0, -0.4, 0.8);
  boomBase.add(cylCase);

  const pistonGeo = new THREE.CylinderGeometry(0.08, 0.08, 1.5, 12);
  const piston = new THREE.Mesh(pistonGeo, chromeSteel);
  piston.rotation.x = Math.PI / 4;
  piston.position.set(0, -0.1, 1.3);
  boomBase.add(piston);

  boomExtend = new THREE.Group();
  boomExtend.position.set(0, 0.2, 4.2);
  boomBase.add(boomExtend);

  const boom2Geo = new THREE.BoxGeometry(0.48, 0.56, 3.8);
  const boom2 = new THREE.Mesh(boom2Geo, craneYellow);
  boom2.position.set(0, 0, 1.8);
  boom2.castShadow = true;
  boomExtend.add(boom2);

  const sheaveGeo = new THREE.CylinderGeometry(0.22, 0.22, 0.45, 16);
  const sheave = new THREE.Mesh(sheaveGeo, chassisDark);
  sheave.rotation.z = Math.PI / 2;
  sheave.position.set(0, -0.1, 3.7);
  boomExtend.add(sheave);

  // Hook Block
  hookGroup = new THREE.Group();
  scene.add(hookGroup);

  const blockGeo = new THREE.BoxGeometry(0.35, 0.5, 0.25);
  const block = new THREE.Mesh(blockGeo, craneYellow);
  block.castShadow = true;
  hookGroup.add(block);

  const hookCurvGeo = new THREE.TorusGeometry(0.25, 0.06, 12, 24, Math.PI * 1.3);
  const hookCurv = new THREE.Mesh(hookCurvGeo, chromeSteel);
  hookCurv.rotation.z = Math.PI / 1.8;
  hookCurv.position.set(0, -0.4, 0);
  hookGroup.add(hookCurv);

  // Cable Line
  const cableGeo = new THREE.BufferGeometry();
  const cablePoints = [new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, -2, 0)];
  cableGeo.setFromPoints(cablePoints);
  const cableMat = new THREE.LineBasicMaterial({ color: 0x38bdf8, linewidth: 2 });
  cableLine = new THREE.Line(cableGeo, cableMat);
  scene.add(cableLine);

  // ================= MASSIVE INDUSTRIAL CONTAINER / CARGO BOX (PER INSTRUCTION) =================
  // Replacing the thin pole with a large heavy industrial container crate!
  suspendedLoad = new THREE.Group();
  hookGroup.add(suspendedLoad);

  // Main Heavy Industrial Container Box (3.8 x 1.8 x 1.8 meters)
  const containerGeo = new THREE.BoxGeometry(3.6, 1.7, 1.7);
  const containerMat = new THREE.MeshStandardMaterial({
    color: 0x1d4ed8, // High-Tech Electric Industrial Blue
    metalness: 0.5,
    roughness: 0.4,
  });
  const containerBox = new THREE.Mesh(containerGeo, containerMat);
  containerBox.position.set(0, -1.5, 0);
  containerBox.castShadow = true;
  containerBox.receiveShadow = true;
  suspendedLoad.add(containerBox);

  // Steel Corner Castings & Reinforced Frame
  const frameGeo = new THREE.BoxGeometry(3.66, 1.76, 1.76);
  const frameMat = new THREE.MeshBasicMaterial({
    color: 0x38bdf8,
    wireframe: true,
  });
  const containerFrame = new THREE.Mesh(frameGeo, frameMat);
  containerFrame.position.set(0, -1.5, 0);
  suspendedLoad.add(containerFrame);

  // 4 Steel Rigging Slings from Hook to Box 4 Corners
  const slingMat = new THREE.LineBasicMaterial({ color: 0xf59e0b, linewidth: 2 });
  const corners = [
    [-1.7, -0.65, -0.8],
    [1.7, -0.65, -0.8],
    [-1.7, -0.65, 0.8],
    [1.7, -0.65, 0.8],
  ];

  corners.forEach(([cx, cy, cz]) => {
    const sGeo = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(0, -0.4, 0),
      new THREE.Vector3(cx, cy, cz),
    ]);
    const sling = new THREE.Line(sGeo, slingMat);
    suspendedLoad.add(sling);
  });

  updateCraneGeometry();
}

function updateCraneGeometry() {
  if (!boomBase || !boomExtend || !hookGroup || !cableLine) return;

  cabinGroup.rotation.y = craneState.rotationY;
  boomBase.rotation.x = -craneState.boomAngle;
  boomExtend.position.z = 4.2 + craneState.boomExtension;

  const tipLocal = new THREE.Vector3(0, -0.1, 3.7);
  const tipWorld = tipLocal.clone();
  boomExtend.localToWorld(tipWorld);

  const hookTarget = tipWorld.clone();
  hookTarget.y = Math.max(1.5, tipWorld.y - craneState.hookHeight);
  hookGroup.position.copy(hookTarget);

  const positions = new Float32Array([
    tipWorld.x, tipWorld.y, tipWorld.z,
    hookTarget.x, hookTarget.y, hookTarget.z,
  ]);
  cableLine.geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  cableLine.geometry.attributes.position.needsUpdate = true;
}

function animate() {
  if (!isCanvasVisible) {
    animFrameId = null;
    return;
  }

  animFrameId = requestAnimationFrame(animate);
  animClock += 0.02;

  if (isDemoMode) {
    craneState.rotationY = Math.sin(animClock * 0.4) * 0.42;
    craneState.boomAngle = 0.33 + Math.sin(animClock * 0.3) * 0.12;
    craneState.boomExtension = 0.8 + Math.sin(animClock * 0.25) * 0.6;
    craneState.hookHeight = 2.4 + Math.sin(animClock * 0.5) * 0.5;

    if (suspendedLoad) {
      suspendedLoad.rotation.z = Math.sin(animClock * 1.5) * 0.02;
    }

    updateCraneGeometry();
  }

  if (controls) {
    controls.update();
  }

  if (renderer && scene && camera) {
    renderer.render(scene, camera);
  }
}

function onWindowResize() {
  const container = document.getElementById('crane-3d-canvas-container');
  if (!container || !renderer || !camera) return;

  isMobileDevice = window.innerWidth < 768 || ('ontouchstart' in window);
  const width = container.clientWidth;
  const height = container.clientHeight || (isMobileDevice ? 420 : 520);

  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
  renderer.setPixelRatio(isMobileDevice ? 1 : Math.min(window.devicePixelRatio || 1, 2));
}

function setupInteractiveControls() {
  const boomSlider = document.getElementById('control-boom-angle');
  const extendSlider = document.getElementById('control-boom-extend');
  const hookSlider = document.getElementById('control-hook-height');
  const rotateSlider = document.getElementById('control-cabin-rotate');
  const demoToggleBtn = document.getElementById('control-demo-toggle');

  if (demoToggleBtn) {
    demoToggleBtn.addEventListener('click', () => {
      isDemoMode = !isDemoMode;
      demoToggleBtn.textContent = isDemoMode ? 'Pause Auto Demo' : 'Start Auto Demo';
      demoToggleBtn.classList.toggle('bg-blue-600', !isDemoMode);
      demoToggleBtn.classList.toggle('bg-slate-800', isDemoMode);
    });
  }

  const handleManualInput = () => {
    if (isDemoMode) {
      isDemoMode = false;
      if (demoToggleBtn) {
        demoToggleBtn.textContent = 'Resume Auto Demo';
        demoToggleBtn.classList.add('bg-blue-600');
        demoToggleBtn.classList.remove('bg-slate-800');
      }
    }
    if (boomSlider) craneState.boomAngle = parseFloat(boomSlider.value);
    if (extendSlider) craneState.boomExtension = parseFloat(extendSlider.value);
    if (hookSlider) craneState.hookHeight = parseFloat(hookSlider.value);
    if (rotateSlider) craneState.rotationY = parseFloat(rotateSlider.value);

    updateCraneGeometry();
  };

  if (boomSlider) boomSlider.addEventListener('input', handleManualInput);
  if (extendSlider) extendSlider.addEventListener('input', handleManualInput);
  if (hookSlider) hookSlider.addEventListener('input', handleManualInput);
  if (rotateSlider) rotateSlider.addEventListener('input', handleManualInput);
}

window.init3DCrane = init3DCrane;
window.setCranePreset = function(type) {
  isDemoMode = false;
  if (type === '12xw') {
    craneState.boomAngle = 0.35;
    craneState.boomExtension = 0.5;
    craneState.hookHeight = 2.0;
  } else if (type === '14xw') {
    craneState.boomAngle = 0.52;
    craneState.boomExtension = 1.9;
    craneState.hookHeight = 2.7;
  } else if (type === 'indus') {
    craneState.boomAngle = 0.42;
    craneState.boomExtension = 1.2;
    craneState.hookHeight = 1.8;
  }
  updateCraneGeometry();
};
