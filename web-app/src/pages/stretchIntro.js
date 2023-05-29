import styles from '@/styles/StretchIntro.module.css'

const StretchIntro = ({
    numSessions,
    breakSecondsLeft
}) => {
    return (
        <>
            <p>Number of sessions left: {numSessions}</p>
            <p className={styles.breakTimer}>Break time left: {Math.floor(breakSecondsLeft / 60)}:{(breakSecondsLeft - (Math.floor(breakSecondsLeft / 60) * 60) < 10) ? 0 : <></>}{breakSecondsLeft - (Math.floor(breakSecondsLeft / 60) * 60)}</p>
            <h2>The Stretches:</h2>
            <div className={styles.stretchContainer}>
                <div className={styles.stretchCard}>
                    <h3>Y-W</h3>
                    <img src="../assets/yw-stretch.svg" alt="the y-w stretch" />
                </div>
                <div className={styles.stretchCard}>
                    <h3>Neck</h3>
                    <img src="../assets/neck-stretch.svg" alt="the neck stretch" />
                </div>
                <div className={styles.stretchCard}>
                    <h3>Side</h3>
                    <img src="../assets/side-stretch.svg" alt="the side stretch" />
                </div>
            </div>
            <button className={styles.readyButton}>READY!</button>
        </>
    );
}

export default StretchIntro;