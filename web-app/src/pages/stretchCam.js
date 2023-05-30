import styles from '@/styles/StretchCam.module.css'
import Webcam from 'react-webcam';

const StretchCam = ({
    numSessions,
    breakSecondsLeft,
    stretchSecondsLeft
}) => {
    return (
        <div className={styles.main}>
            <p>Number of sessions left: {numSessions}</p>
            <p className={styles.breakTimer}>Break time left: {Math.floor(breakSecondsLeft / 60)}:{(breakSecondsLeft - (Math.floor(breakSecondsLeft / 60) * 60) < 10) ? 0 : <></>}{breakSecondsLeft - (Math.floor(breakSecondsLeft / 60) * 60)}</p>
            <div className={styles.camContainer}>
                <Webcam style={{
                    width: 640, height: 480, position: "absolute",
                  
                    zIndex: 1
                }} />
                <canvas style={{
                    width: 640, height: 480,
                    
                    zIndex: 2
                }} />
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