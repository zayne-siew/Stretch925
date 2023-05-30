import styles from '@/styles/StretchCam.module.css'
import Webcam from 'react-webcam';
import React, { useRef } from "react";
import * as tf from "@tensorflow/tfjs";
import * as posenet from "@tensorflow-models/posenet";
import { drawKeypoints, drawSkeleton } from "../pages/utilities";

const StretchCam = ({
    numSessions,
    breakSecondsLeft,
    stretchSecondsLeft,
    skipTimer
}) => {

    const webcamRef = useRef(null);
    const canvasRef = useRef(null);

    //  Load posenet
    const runPosenet = async () => {
        const net = await posenet.load({
        inputResolution: { width: 640, height: 480 },
        scale: 0.8,
        });
        //
        setInterval(() => {
        detect(net);
        }, 100);
    };

    const detect = async (net) => {
        if (
            typeof webcamRef.current !== "undefined" &&
            webcamRef.current !== null &&
            webcamRef.current.video.readyState === 4
        ) {
            // Get Video Properties
            const video = webcamRef.current.video;
            const videoWidth = webcamRef.current.video.videoWidth;
            const videoHeight = webcamRef.current.video.videoHeight;

            // Set video width
            webcamRef.current.video.width = videoWidth;
            webcamRef.current.video.height = videoHeight;

            // Make Detections
            const pose = await net.estimateSinglePose(video);
            console.log(pose);

            drawCanvas(pose, video, videoWidth, videoHeight, canvasRef);
        }
    };

    const drawCanvas = (pose, video, videoWidth, videoHeight, canvas) => {
        const ctx = canvas.current.getContext("2d");
        canvas.current.width = videoWidth;
        canvas.current.height = videoHeight;

        drawKeypoints(pose["keypoints"], 0.6, ctx);
        drawSkeleton(pose["keypoints"], 0.7, ctx);
    };

    runPosenet();

    return (
        <div className={styles.main}>
            <p>Number of sessions left: {numSessions}</p>
            <p className={styles.breakTimer}>Break time left: {Math.floor(breakSecondsLeft / 60)}:{(breakSecondsLeft - (Math.floor(breakSecondsLeft / 60) * 60) < 10) ? 0 : <></>}{breakSecondsLeft - (Math.floor(breakSecondsLeft / 60) * 60)}</p>
            <div className={styles.camContainer}>
                <Webcam
                    ref={webcamRef}
                    style={{
                        position: "absolute",
                        textAlign: "center",
                        zindex: 1,
                        width: 640,
                        height: 480,
                    }}
                />
                <canvas
                    ref={canvasRef}
                    style={{
                        textAlign: "center",
                        zindex: 2,
                        width: 640,
                        height: 480,
                    }}
                />
            </div>

            <div className={styles.infoContainer}>
                <div className={styles.leftBoxesContainer}>
                    <div className={styles.scoreBox}>
                        <p>Score</p>
                        <h1>120</h1>
                    </div>
                    <div className={styles.timeBox}>
                        <p>Time Left</p>
                        <h1>{stretchSecondsLeft}</h1>
                    </div>
                    <button className={styles.skipButton} onClick={()=>skipTimer("stretch")}>SKIP</button>
                </div>

                <div className={styles.stretchesBox}>
                    <div className={styles.stretch}>
                        <img src="../assets/yw-stretch.svg" alt="" />
                        <p>Y-W</p>
                    </div>
                    <div className={styles.stretch}>
                        <img src="../assets/neck-stretch.svg" alt="" />
                        <p>Neck</p>
                    </div>
                    <div className={styles.stretch}>
                        <img src="../assets/side-stretch.svg" alt="" />
                        <p>Side</p>
                    </div>
                </div>
            </div>

        </div>
    );
}

export default StretchCam;